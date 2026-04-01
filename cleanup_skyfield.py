import sys

filepath = 'apts/skyfield_searches.py'
with open(filepath, 'r') as f:
    lines = f.readlines()

new_lines = []
skip = False
found_mutual = False

for line in lines:
    if line.startswith('def find_jovian_mutual_events'):
        if not found_mutual:
            found_mutual = True
            new_lines.append(line)
        else:
            skip = True
    elif line.startswith('def find_jovian_moon_events'):
        skip = False
        new_lines.append(line)
    elif not skip:
        new_lines.append(line)

# Also fix get_timescale() efficiency in both functions
content = "".join(new_lines)
content = content.replace(
    "            t_eval = get_timescale().tt_jd(t.tt - pos_sj.light_time)",
    "            t_eval = ts.tt_jd(t.tt - pos_sj.light_time)"
)

# Ensure 'ts' is available in find_jovian_moon_events scope for state_func
content = content.replace(
    "    ts = get_timescale()\n    t0 = ts.utc(start_date)\n    t1 = ts.utc(end_date)",
    "    ts = get_timescale()\n    t0 = ts.utc(start_date)\n    t1 = ts.utc(end_date)"
) # It's already there.

with open(filepath, 'w') as f:
    f.write(content)
