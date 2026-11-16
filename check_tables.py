"""Cell-count and cross-check validator for silver-thesis-key-milestones.html.
Run:  python -I check_tables.py [path]      Exit code 1 if any problem is found.
"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = sys.argv[1] if len(sys.argv) > 1 else 'silver-thesis-key-milestones.html'
s = open(path, encoding='utf-8').read()
problems = []

def strip(x):
    return re.sub(r'<[^>]+>', '', x).replace('&#8212;', '-').strip()

def table_after(marker):
    i = s.index(marker)
    j = s.index('</table>', i)
    return s[i:j]

def check_cells(name, blk):
    ths = len(re.findall(r'<th[\s>]', blk.split('</thead>')[0]))
    counts = {}
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', blk.split('</thead>', 1)[-1], re.S):
        if 'row-group' in tr or 'colspan' in tr:
            continue
        tds = re.findall(r'<td', tr)
        if tds:
            counts.setdefault(len(tds), []).append(strip(tr.split('</td>')[0])[:30])
    ok = len(counts) == 1 and (not ths or list(counts)[0] == ths)
    print(('OK  ' if ok else 'FAIL'), name, 'header cols=%d' % ths, {k: len(v) for k, v in counts.items()})
    if not ok:
        problems.append(name)
        for k, v in counts.items():
            print('     %d cells:' % k, v[:6])

for sec in ['ds-inventory', 'ds-curve', 'ds-premiums', 'ds-positioning', 'ds-demand']:
    check_cells(sec, table_after('id="%s"' % sec))
check_cells('mds', table_after('class="mds-table"'))

# Reg/Eligible must equal Registered / Eligible (+-0.02) in every month column
blk = table_after('id="ds-inventory"')
rows = {}
for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', blk, re.S):
    tds = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)
    if tds:
        rows[strip(tds[0])[:12]] = [strip(t).lstrip('~') for t in tds[1:]]
hdr = [strip(h) for h in re.findall(r'<th[^>]*>(.*?)</th>', blk, re.S)][1:]
R, E, X = rows.get('COMEX Regist'), rows.get('COMEX Eligib'), rows.get('Registered /')
if R and E and X:
    for h, r, e, x in zip(hdr, R, E, X):
        try:
            if abs(float(r) / float(e) - float(x)) > 0.03:
                problems.append('ratio ' + h)
                print('FAIL ratio %s: %s/%s=%.2f vs %s' % (h, r, e, float(r) / float(e), x))
        except ValueError:
            pass

print('\nPROBLEMS:' if problems else '\nAll checks passed.', problems or '')
sys.exit(1 if problems else 0)
