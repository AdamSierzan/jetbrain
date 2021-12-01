num_list = []
while True:
    number = int(input())
    if number == 55:
        break
    else: 
        num_list.append(number)
        continue

    
print(len(num_list))
print(sum(num_list))
print(round(len(num_list)/sum(num_list)))
