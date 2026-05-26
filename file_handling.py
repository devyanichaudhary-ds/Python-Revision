#Create a text file.
file=open("Sample.txt","w")
file.write("Hello World!!")
file.close()


#Read Entire File.
file = open("Sample.txt","r")
content = file.read()
print(content)
file.close()


#Read File Line by Line.
file = open("Sample.txt","r")
for line in file:
    print(line.strip())
file.close()


#Count Words in a File.
file =open("Sample.txt","r")
content=file.read()
words=content.split()
print("Words:",len(words))
file.close()


#Count Lines in a File.
file = open("Sample.txt","r")
count=0
for line in file:
    count +=1
print("lines:",count)
file.close()


#Count Characters in a File
file = open("Sample.txt","r")
content = file.read()
print("Characters:",len(content))
file.close()


#Append Text to a File
file =open("Sample.txt","a")
file.write("\nIts a file handling program")
file.close()


#Copy Contents to Another File
source = open("Sample.txt","r")
content = source.read()
destination=open("copy.txt","w")
destination.write(content)
source.close()
destination.close()


#Search a Word in a File.
word=input("enter a text:")
file=open("Sample.txt","r")
content=file.read()
if word in content:
    print("word found")
else:
    print("word not found")
file.close()


#Create Student Record File
name=input("enter name:")
marks=input("enter marks:")
file = open("Student.txt","a")
file.write(f"{name}-{marks}\n")
file.close()
print("Record Saved")