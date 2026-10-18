mobile=['poco','redmi','iphone','vivo','samsung','realme']
for index, phone in enumerate(mobile):
    print(f"index {index},phone {phone}")
school=['maner','patna','shantinager','road side', 'villager student']
for index, place in enumerate (school,2):
    print(f"index {index},place {place}")
names=['Prince','neo','synapse','prince neo synapse']
marks=[100,99,99,98]
for name, mark in zip(names,marks):
    print(f"name {name} got {mark} marks")
#normal
even_number = [ ]
for num in range(41):
   if num % 2 == 0:
       even_number.append(num)
print(even_number)
odd_number=[ ]
for num in range(5):
    if num%2 !=0:
        odd_number.append(num)
print(odd_number)
odd_number=[num for num in range(125)if num%1==0]
print('natural numbers',odd_number)
even_numbers=[num for num in range(21)
if num % 2==0]
print(even_numbers)
numbers=[0,1,2,3,4,5,6,7,8,9]
even_numbers=[num for num in numbers
if num % 2==0]
print(even_numbers)
