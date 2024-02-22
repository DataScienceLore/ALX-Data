for i in range(5):
  print(i) # Prints 0, 1, 2, 3, 4

def bubble_sort(items):
    n = len(items)
    while True:
        swapped = False
        for i in range(1, n):
            if items[i - 1] > items[i]:
                items[i - 1], items[i] = items[i], items[i - 1]
                swapped = True
        if not swapped:
            break
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)

'''
Rearrange the following lines to correctly implement a bubble sort algorithm for a list.

What is the output if…
'''

def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
#Implementation of bubble sort.
               items[j], items[j+1] = items[j+1], items[j]

    return items

my_list = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(my_list)

print("Sorted list:", my_list)



class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

account = BankAccount(100)  # Create an account with initial balance of 100
account.deposit(50)        # Deposit 50 into the account
print(account.balance)     # Print the updated balance

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

circle = Circle(3)  # Create a Circle object with radius 3
circumference = circle.circumference()  # Calculate the circumference
print(f"Circumference of the circle: {circumference:.2f}")  # Print the result

#Identify the line that violates the PEP 8 style guidelines:

class ExampleClass:
    def __init__(self,value):
        self.value = value
    def get_value(self):
        return self.value
