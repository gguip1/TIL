T = 9

MAX = None
MAX_LOCATION = None

for i in range(T):
    
    value = int(input())
    
    if MAX is None:
        MAX = value
        MAX_LOCATION = i + 1
    
    if value > MAX:
        MAX = value
        MAX_LOCATION = i + 1

print(MAX)
print(MAX_LOCATION)
