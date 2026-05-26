#Create a set.
S={1,4,5,6,7}
print(S)

#Remove duplicates from a list using set.
S=[1,4,5,5,6,6,7]
unique_set = set(S)
unique_list = list(unique_set)
print(unique_list)

#Find union.
S={1,4,5,6,7}
P=S.union({12,13})
print(P)

#Find intersection.
S={12,13,4,5,6,7}
P=S.intersection({12,13})
print(P)

#Find difference.
S={12,13,4,5,6,7}
P={12,13}
d=S-P
print(d)

#Check subset.
A={1,2,3}
B={1,2,3,4,5,6,7}
if A.issubset(B):
    print("A is a subset of B.")
else:
    print("A is not a subset of B.")

#Check Superset.
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}

if A.issuperset(B):
    print("A is a superset of B")
else:
    print("A is not a superset of B")

#Find Symmetric Difference.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
result = A.symmetric_difference(B)
print(result)
#OR
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)

#Count Unique Words in a Sentence.
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
unique_words = set(words)
print("Unique words:", len(unique_words))
print(unique_words)

#Compare Two Sets.
A = {1, 2, 3}
B = {3, 2, 1}

if A == B:
    print("Sets are equal")
else:
    print("Sets are not equal")