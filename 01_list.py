"Introduction to list."

# Define list?
# Basically, list are containers to store a set of values of any data type.

# list1 is the list of six even numbers.
# list1 = [2,4,6,8,10,12]
# print(list1)
# Output:
# [2, 4, 6, 8, 10, 12].

# list4 is the list of lists called nested list.
# list4 = [['Physics',101],['Chemistry',202],['Maths',303]]
# print(list4)
# Output:
# [['Physics', 101], ['Chemistry', 202], ['Maths', 303]].


"Accessing elements in a list."

# list1 = [2,4,6,8,10,12]
# print(list1[0])
# Output: 2  
# return first element of list1.

# print(list1[15]) 
# Output: IndexError: list index out of range

# print(list1[1+4])
# Output: 12

# print(list1[-1])
# Output: 12

# print(len(list1))
# Output: 6 
# returns the length of the list.

"Lists are mutable."
# Yes,in python lists are mutable. It means that the contents of the list can be changed after it has been created. 
# For ex:
# List1 = ["Jatin","Srijan","Maithly","Ada","Vani","Armaan","Kanishka","Faaz"]
# List1[7] = "Mayank"
# print(List1)
# Output: ['Jatin', 'Srijan', 'Maithly', 'Ada', 'Vani', 'Armaan', 'Kanishka', 'Mayank'].

"Concatenation."
# Python allow us to join two or more lists using concatenation operator by the symbol + .
# List1 = [1,3,5,7,9]
# List2 = [2,4,6,8,10]
# List1 + List2
# print(List1 + List2)
# Output: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10].

"Repetion."
# Python allows to replicate a list using repetion operator by the symbol *.
# List1 = ['Forest']
# List1*5
# print(List1*5)
# Output: ['Forest', 'Forest', 'Forest', 'Forest', 'Forest'].

"Membership."
# The membership operators checks if the element is present in the list and returns True, else returns False.
# List1 = ['Jonathan','ZGod','Action']
# print('ZGod' in List1)
# Output: True
# print('Ghatak' in List1)
# Output: False.

"Slicing."
#List1 = ['Red','Yellow','Black','Pink','White','Blue','Brown']
# print(List1[2:6])
# Output: ['Black', 'Pinnk', 'White', 'Blue']
# print(List1[2:20])
# Output: ['Black', 'Pinnk', 'White', 'Blue', 'Brown']
# print(List1[7:2])
# Output: [] # empty list. Because first index is > than second index.
# print(List1[:5])
# Output: ['Red', 'Yellow', 'Black', 'Pinnk', 'White'].
# print(List1[0:6:2])
# Output: ['Red', 'Black', 'White'].
# print(List1[-6:-2])
# Output: ['Yellow', 'Black', 'Pink', 'White'].
# print(List1[::2])
# Output: ['Red', 'Black', 'White', 'Brown'].
# print(List1[::-1])
# Output: ['Brown', 'Blue', 'White', 'Pink', 'Black', 'Yellow', 'Red'].

"Traversing the list."

#(a) List traversal using For loop.
# List1 = ['Mango','Apple','Lichi','Guava','Chicku']
# for item in List1:
#    print(item)
# Output: Mango
#         Apple
#         Lichi
#         Guava
#         Chicku.
# print(len(List1))
# Output: 5.

# (b) List traversal using while loop:
# List1 = ['Mango','Apple','Lichi','Guava','Chicku']
# i = 0
# while i < len(List1):
#    print(List1[i])
#    i = 2

"List methods and functions."

#len()- Returns the length of the list.
# For ex-
# List1 = [10,20,30]
# print(len(List1))
# Output: 3.

#List()- Creates an empty list if the list has no characters or integers.
# For ex-
# List1 = []
# print(List1)
# Output: []
#         Creates a list if the argument is there.
# For ex-
# List1 = ['Jatin']
# print(List1)
# Output: ['Jatin'].

#Append()- This function is used to add items at the end of the string.
# For ex- 
# List1 = [100,200,300,400,500]
# List1.append(600)
# print(List1)
# Output: [100, 200, 300, 400, 500, 600].
#          The single element also be a list.
# For ex-
# List1 = [100, 200, 300, 400, 500, 600]
# List1.append([700,1000])
# print(List1)
# Output: [100, 200, 300, 400, 500, 600, [700, 1000]]

#Extend()- This function is used for adding multiple times. This function only add list to any list. Single value can't add using extend().
# For ex-
# List1 = [3,4,5,6,7]
# List2 = [8,9,10]
# List1.extend(List2)
# print(List1)
# Output: [3, 4, 5, 6, 7, 8, 9, 10]

#Insert()- Inserts an element at a particular index in the list.
# For ex-
# List1 = [1,2,3,4,5,6]
# List1.insert(4,7)
# print(List1)
# Output: [1, 2, 3, 4, 7, 5, 6].

#Count()- Returns the number of times a given element appears in the list.
# For ex-
# List1 = [9,8,9,7,6,5,4,8,5,6,5]
# print(List1.count(5))
# Output: 3

#Index()- Returns index of the first occurance of the element in the list. If the element is not present, Value error is generated.
# For ex-
# List1 = [1,2,3,4,5,6]
# print(List1.index(5))
# Output: 4
# List1 = [1,2,3,4,5,6]
# print(List1.index[8])
# Output: TypeError: 'builtin_function_or_method' object is not subscriptable.

#Remove()- Removes the given element from the list. If the element is present multiple times, only the first occurance is removed. If the element is not present, then the value error is generated.
# For ex-
# List1 = [10,20,30,40,50,30,30]
# print(List1.remove(30))
# print(List1)
# Output: [10, 20, 40, 50, 30, 30]

#Pop()- This function is used to remove the item from list.
# For ex-
# List1 = [10,20,30,40,50]
# print(List1.pop(1))
# print(List1)
# Output: [10, 30, 40, 50]

#Reverse()- Reverses the order of elements in the given list.
# For ex-
# List1 = [11,12,13,14,15,16]
# List1.reverse()
# print(List1)
# Output: [16, 15, 14, 13, 12, 11].

#Sort()- Sorts the elements of the given list in-place.
# For ex-
# List1 = ['Jatin','Srijan','Maithly','Kanishka','Vani','Ada','Armaan','Mayank']
# List1.sort()
# print(List1)
# Output: ['Ada', 'Armaan', 'Jatin', 'Kanishka', 'Maithly', 'Mayank', 'Srijan', 'Vani'].

#Sorted()- It takes a list and creates a new list consisting of the same elements arranged in sorted order.
# For ex- 
# List1 = [56,35,34,78,12,1,100]
# List2 = sorted(List1)
# print(List2)
# Output: [1, 12, 34, 35, 56, 78, 100].

#Min()- Returns minimum or smallest element of the list.
# For ex-
List1 = [12,4,2,56,78]
min(List1)
print(List1)












    






















         


