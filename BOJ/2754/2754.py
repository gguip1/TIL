score = input()

if score == 'A+':
    result = 4.3
elif score == 'A0':
    result = 4.0
elif score == 'A-':
    result = 3.7
elif score == 'B+':
    result = 3.3
elif score == 'B0':
    result = 3.0
elif score == 'B-':
    result = 2.7
elif score == 'C+':
    result = 2.3
elif score == 'C0':
    result = 2.0
elif score == 'C-':
    result = 1.7
elif score == 'D+':
    result = 1.3
elif score == 'D0':
    result = 1.0
elif score == 'D-':
    result = 0.7
else:
    result = 0.0

print(result)
