'''
def mul_five_times(number):
    return  number *5
result =[]
num =[3,5,7,9,2,1,5]
for i in num:
    result.append(mul_five_times(i))
print(result)
out 1 : [15, 25, 35, 45, 10, 5, 25]
'''
# out 2: [15, 25, 35, 45, 10, 5, 25]
def mul_five_times(number):
    return number * 5
num = [3,5,7,9,2,1,5]
result = list(map(mul_five_times , num))
print(result)