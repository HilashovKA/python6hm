line = 'ооррроррооор'
max_len = 0
while True:
    if 'о' in line:
        start = line.index('о')
    else:
        break
    if 'р' in line[start:]:
        end = line.index('р', start)
        max_len = max(max_len, len(line[start:end]))
    else:
        max_len = max(max_len, len(line[start:]))
        break
    line = line[end + 1:]
 
print(max_len)