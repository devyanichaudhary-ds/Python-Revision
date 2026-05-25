#find largest element.
number=[16,42,63,67,54,34]
largest_number=max(number)
print("the largest element is: ",largest_number)


#Find smallest element.
numbers=[12,34,56,75,86]
smallest_element=min(numbers)
print("the smallest element is: ",smallest_element)


#Remove duplicates.
l=[11,11,13,23,33,23,43]
unique_number=list(set(l))
print(unique_number)


#Reverse a list.
q=[12,22,3,34,21,87]
q.reverse()
print(q)


#Sort without using sort().
numbers = [5, 2, 8, 1, 9]
n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Sorted List:", numbers)


#Find the Second Largest Number.
numbers = [12, 35, 1, 10, 34, 35, 1]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print("Second largest:", second_largest)
else:
    print("Not enough unique elements")


#Merge Two Lists.
l1= [12,23,34,43,54]
l2= [23,34,52,21,34]
merge=l1+l2
print("Merged List: ",merge)


#Count Frequency of Each Element.
numbers=[12,33,43,43,23,12,67,65]
frequency={}
for n in numbers:
    if n in frequency:
        frequency[n] +=1
    else:
        frequency[n] = 1
print(frequency)


#Rotate List by One Position.
numbers=[12,34,22,54,44,57]
numbers=[numbers[-1]] + numbers[:-1]
print(numbers)


#Separate Even and Odd Numbers.
s=[12,23,43,45,56,76]
for n in s:
    if n%2==0:
        print("Even:",n)
    else:
        print("Odd:",n)
# OR
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)