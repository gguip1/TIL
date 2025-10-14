colors = [input() for _ in range(3)]
color_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

answer = 0
for index, color in enumerate(colors):
    for check_index, check_color in enumerate(color_list):
        if color == check_color:
            value = check_index
            product = 10 ** check_index
    
    if index == 0:
        answer += 10 * value
    elif index == 1:
        answer += value
    else:
        answer *= product

print(answer)