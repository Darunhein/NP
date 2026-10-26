"""

Methods for Lists : 

append(value) : Adds an item to the end of the list.    
insert(index, value) : Adds an item at the specified index.
extend(value, start, end) : Adds multiple values to the end of the list.
count(value, start, end) : Returns the number of times a value appears in the list.
index(value, start, end) : Returns the index of the first occurrence of a value.
sort(key=None, reverse=False) : Sorts the list in ascending order.
reverse(start, end) : Reverses the order of the elements in the list.
remove(value, start, end) : Removes the first occurrence of a value.
pop(index, start, end) : Removes and returns the element at the specified index.

Examples : 

colors.append('Gold')
colors.extend(['Gold','Silver'])
colors.insert(0,'Gray')
colors.clear()
colors.append('Violet')
print(colors.pop(0))
print(colors.sort(reverse=False))
print(colors.sort(reverse=True))
colors_1=colors.copy()

"""

#Lists :
nums=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
colors=['Red','Green','Yellow','Blue','Black','White','Orange','Purple','Pink','Brown']

#First Prints : 
print(nums)
print(colors)

#First For Loop (Prints the output directly) : 
for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    print(output)

#Reversing the list : 
nums.reverse()
for num in nums:
    output1 = f"[{num}, {colors[nums.index(num)]}]"
    print(output1)

#Second for loop (Appends the output to a list) :
nums.reverse()
output2 = []
for num in nums:
    output1 = f"[{num}, {colors[nums.index(num)]}]"
    output2.append(output1)

#Final List Print : 
print(output2)

