result = []

while True:
    name, age, weight = input().split()
    
    age = int(age)
    weight = int(weight)
    
    if name == "#" and age == 0 and weight == 0:
        break
    
    if age > 17 or weight >= 80:
        result.append(name + ' Senior')
    else:
        result.append(name + ' Junior')

for r in result:
    print(r)
