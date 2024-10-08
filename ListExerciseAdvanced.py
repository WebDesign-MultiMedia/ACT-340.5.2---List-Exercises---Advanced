# Problem 1
print("Problem 1")
clothing = ['socks', 'pants', 'shirt', 'polo']
print(clothing)
clothing.insert(4, 'skirt', )
print(clothing, ': insert method')
print('')

# Problem 2
print("Problem 2")
print(clothing)
clothing.insert(2,['suit jacket', 'suit pants', 'tie', 'buttom down'])
print(clothing, ': insert method')
print('')

# Problem 3
print("Problem 3")
nums = [2, 150, 14, 36, 78, 81, 14, 1000, 54, 14, 14]
print(nums.count(14), ': count method')
print(nums.count(2), ': count method')
print(' ')

# Problem 4
print("Problem 4")
print(sum(nums), ': sum method')
print(' ')

# Problem 5
print("Problem 5")
#Slice the list so that it is reversed without using the .reverse() method
print(nums[::-1], ': slice method')
print(' ')

# Problem 6
print("Problem 6")
one_to_five = [1,2,3,4,5]
print(one_to_five[-2:], ': slice method')
print(' ')

# Problem 7
print("Problem 7")
animals = ['koala', 'cat', 'fox', 'panda', 'chipmunk', 'sloth']
print(animals)
print('"For Loop: List"')
for all in animals:
    print(all)
print(' ')

# Problem 8
print("Problem 8")
random_things = ['hello', ['breakfast', 'you', 'prncil', 2], 22, ['burrito', 'taco'], [22, 'win', 33,[5], 'laptop']]
print(random_things, ': random')
print('')
def funcArg(list):
    for all in list:
        print(all, type(all))
funcArg(random_things)
print(' ')

# Problem 9
print("Problem 9")
names = ['Dre', 'Seuss', 'Who', 'McCoy']
Doctors = []
for name in names:
    Doctors.append("Dre. " + name)
    print(Doctors)
print(' ')
newList = []
for newName in names:
    newList.append(newName + " Who")
    print(newList)
print(' ')  

# Problem 10
print("Problem 10")
num2 = [10, 99, 85, 76, 43, 2, 77, 100, 13, 12, 42, 99, -1, -100]
print(num2 , ': original')

index = 0
while index < len(num2):
    if num2[index] == 100:
        print(f"100 is at index {index}")
        break
    index += 1
print(' ')

# Problem 11
print("Problem 11")
list1 =["McDonalds", "Wendy's", "Burger King" "", "Taco Bell"]
new_list = []
for i in list1:
    if i:
        new_list.append(i)
print(new_list)
print(' ')

my_list = [1,2,3]
another_list = [4,5,6]
my_list.extend(another_list)
print(my_list, another_list, ': extend method')

another_list.append(7)
print(my_list, another_list, ': append method')