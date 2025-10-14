import sys
input = sys.stdin.readline

N = int(input())
strings = [input().strip() for n in range(N)]

def get_vaccine(string:str, strings:list):
    if len(strings) == 0:
        return [string]
    
    results = []
    for index, add_string in enumerate(strings):
        string_copy = strings.copy()
        string_copy.pop(index)
        
        k = 0
        for i in range(min(len(string), len(add_string))):
            if string[-(i + 1):] == add_string[:(i + 1)]:
                k = (i + 1)
        if k != 0:
            results.extend(get_vaccine(string + add_string[k:], string_copy))
        else:
            continue
    
    return results

results = []

for index, string in enumerate(strings):
    strings_copy = strings.copy()
    strings_copy.pop(index)
    
    results.extend(get_vaccine(string, strings_copy))

print(len(min(results, key=len)))
