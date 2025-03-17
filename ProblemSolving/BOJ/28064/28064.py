import sys

N = int(sys.stdin.readline().rstrip())

names = [sys.stdin.readline().rstrip() for _ in range(N)]

result = 0

for index, name in enumerate(names[:-1]):
    for target in names[index + 1:]:
        i_got_it = False
        
        for i in range(len(name)):
            if name[:i + 1] == target[-i - 1:]:
                i_got_it = True
            
            if i_got_it:
                break
        
        i_got_it_reverse = False
        
        for i in range(len(name)):
            if name[-i - 1:] == target[:i + 1]:
                i_got_it = True
            
            if i_got_it:
                break
        
        # print(name, target, end=' : ')
        # print(i_got_it, i_got_it_reverse)
        
        if i_got_it or i_got_it_reverse and not (i_got_it and i_got_it_reverse):
            result += 1
                

print(result)