n = int(input())
nums = [int(input()) for _ in range(n)]

stack = []
result_stack = []
result = []

r = 0

push_stop = False

for num in nums:
    for i in range(r, n):
        if stack:
            print(i, stack, num, stack[len(stack) - 1])
            if num == stack[len(stack) - 1]:
                result.append('-')
                result_stack.append(stack[len(stack) - 1])
                stack.pop()
                r = i
                break
        
        if not push_stop:
            result.append('+')
            stack.append(i + 1)
        
        if i + 1 == n:
            push_stop = True
        

print(nums)
print(result_stack)

if nums == result_stack:
    for _ in result:
        print(_)
else:
    print('NO')
