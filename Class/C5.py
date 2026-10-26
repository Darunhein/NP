"""
Made by: Darius_Pasoch
Exercise 11/09/2026:
1 Create a function that allows entering elements into a list within a FOR loop.
2 Create a function that allows entering elements into a dictionary within a FOR loop.
3 Create a function that allows printing all elements of a list and a dictionary within a FOR loop.
"""


#1 Create a function that allows entering elements into a list within a FOR loop.
def Funct1():
    list1 = []
    for i in range(0,10,2):
        list1.append(i)
    return list1
print(Funct1())

# Secondary way (using parameters and print instead of return)
def Funct1_v2(start, end, step):
    list1 = []
    for i in range(start, end, step): 
        list1.append(i) # The function saves the values in a list.
    print(list1)
    
Funct1_v2(0, 10, 3)


#2 Create a function that allows entering elements into a dictionary within a FOR loop.
def Funct2(number):
    dict1 = {}
    print(f"This is the multiplication table for {number}:")
    for i in range(1, 11): # Loops from 1 to 10
        dict1[i] = number * i # Saves the result in the dictionary where 'i' is the key
        print(f"{number} * {i} = {dict1[i]}")

Funct2(4) # Will print the multiplication table for 4

#3 Create a function that allows printing all elements of a list and a dictionary within a FOR loop.
def Funct3(my_list, my_dict):
    print("--- Using Zip with Parameters ---")
    # zip pairs a list item with a (key, value) dictionary item
    for list_item, (dict_key, dict_value) in zip(my_list, my_dict.items()):
        print(f"List item: {list_item} | Dict -> Key: {dict_key}, Value: {dict_value}")

# Example usage with variables
sample_list = ["Apple", "Banana", "Cherry"]
sample_dict = {1: "Red", 2: "Yellow", 3: "Dark Red"}

Funct3(sample_list, sample_dict)