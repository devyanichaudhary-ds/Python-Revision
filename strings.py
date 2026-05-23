#Count vowels in a string.
c='abacus'
count =0
for ch in c.lower():
    if ch in "aeiou":
        count+=1
print("number of vowels:",count)

#Reverse a string.
s="octopus"
print("reversed string:",s[::-1])

#Check if a String is a Palindrome
x="madam"
if x==x[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#Count Uppercase and Lowercase Letters.
f="For YOUR Information"
upper=0
lower=0
for ch in f:
    if ch.isupper():
        upper +=1
    elif ch.islower():
        lower +=1
print("uppercase letters:",upper)
print("lowercase letters:",lower)

#Replace Spaces with Hyphens.
d="hi my name is devyani."
q=d.replace(" ","-")
print(q)

#Count Occurrences of a Character.
text="hello world i am writing code"
count = text.count("w")
print("occurences:",count)

#Remove All Vowels from a String.
p="hello horsehouse"
result=""
for ch in p:
    if ch.lower() not in "aeoiu":
        result+=ch
print(result)

#Find the Longest Word in a Sentence.
sentence ="python is a powerful programming language."
word= sentence.split()
longest=max(word, key=len)
print("longest word:", longest)

#Convert First Letter of Every Word to Uppercase.
y="best way to learn is practice"
print(y.title())

#Check if Two Strings are Anagrams.
str1="heart"
str2="earth"
if sorted(str1.lower())==sorted(str2.lower()):
    print("Anagram")
else:
    print("Not Anagram")