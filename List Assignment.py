# Exercise_1: Create a list of 5 of your favorite fruits. Print the list.

# Solution_1
fruits = ["apple", "mandarin", "mango", "watermelon", "grapes"]
print(fruits)

# Exercise_2: Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list.

# Solution_2
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[4])

# Exercise_3: Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list.

# Solution_3
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

# Exercise_4: Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset.

# Solution_4
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
print(names[0:3])

# Exercise_5: Create a list of numbers from 1 to 10 and use a loop to print each number squared.

# Solution_5
base_numbers = [1,2,3,4,5,6,7,8,9,10]
output = []
for val in base_numbers:
    output.append(val**2)
print(output)

# Exercise_6: Create an empty list called shopping_cart. 
# Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. 
# Print the final list.

# Solution_6
shopping_cart = []
additionals = ["butter","cheese"]
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
shopping_cart.extend(additionals)
print(shopping_cart)

# Exercise_7: Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33].

# Solution_7
numbers_2 = [45, 22, 88, 56, 92, 33]
print("Maximum value:", max(numbers_2))
print("Minimum value:", min(numbers_2))

# Exercise_8: Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list.

# Solution_8
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
how_many_a = letters.count('a')
print("How many a's?:", how_many_a)

# Exercise_9: Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.

# Solution_9
def squares(start,end):
     squares = [value * 2 for value in range(start,end+1)]
     return squares
print(squares(0,5))

# Exercise_10: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.

# Solution_10
list_nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

list_nums = list(set(list_nums))
print(list_nums)