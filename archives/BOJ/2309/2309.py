import sys

dwarf = [int(sys.stdin.readline().strip()) for _ in range(9)]

dwarf_copy = dwarf.copy()

for i in range(len(dwarf)):
    for j in range(len(dwarf) - 1):
        dwarf_copy.pop(i)
        dwarf_copy.pop(j)
        if sum(dwarf_copy) == 100:
            break
        else:
            dwarf_copy = dwarf.copy()
    if sum(dwarf_copy) == 100:
        break

dwarf_copy.sort()

for d in dwarf_copy:
    print(d)
