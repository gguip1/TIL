import sys
input = sys.stdin.readline

call_signs = [
    'se no hai- hai- hai hai hai u- hai'.split(),
    'mik-jjang kawaii!'.split(),
    'Are you ready antena senku high!'.split(),
    'u- hai'.split(),
    'hai'.split()
]

S = input().split()

index = 0
answer = [0, 0]

while index < len(S):
    if S[index] == call_signs[0][0]:
        answer[0] += 1
        answer[1] += 1
        call_sign_index = 1
        while call_sign_index < len(call_signs[0]):
            if S[index] == call_signs[0][call_sign_index]:
                call_sign_index += 1
            index += 1

        u_hai_index = 0
        u_hai = ['u-', 'hai']
        
        while index < len(S):
            if u_hai_index % 2 == 0:
                if S[index] in ['se', 'mik-jjang', 'Are', 'hai']:
                    break
                else:
                    if S[index] == u_hai[u_hai_index % 2]:
                        u_hai_index += 1
                    index += 1
            else:
                if S[index] == u_hai[u_hai_index % 2]:
                    u_hai_index += 1
                index += 1
    elif S[index] == call_signs[1][0]:
        answer[0] += 1
        answer[1] += 1
        call_sign_index = 1
        while call_sign_index < len(call_signs[1]):
            if S[index] == call_signs[1][call_sign_index]:
                call_sign_index += 1
            index += 1
    elif S[index] == call_signs[2][0]:
        answer[0] += 1
        answer[1] += 1
        call_sign_index = 1
        while call_sign_index < len(call_signs[2]):
            if S[index] == call_signs[2][call_sign_index]:
                call_sign_index += 1
            index += 1
    elif S[index] == call_signs[3][0]:
        answer[1] += 1
        call_sign_index = 1
        while call_sign_index < len(call_signs[3]):
            if S[index] == call_signs[3][call_sign_index]:
                call_sign_index += 1
            index += 1
    elif S[index] == call_signs[4][0]:
        answer[1] += 1
        index += 1
    else:
        index += 1

print(*answer)