#Create student dictionary.
student={ "name":"devyani",
         "class":"12th",
         "roll no":"11"}
print(student)


#Print all keys.
k={"name":"yashika",
   "sem":"6"}
print(k.keys())


#Print all values.
k={"name":"yashika",
   "sem":"6"}
a=k.items()
print(a)


#Count frequency of characters in a string.
text=input("enter text:")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)


#Merge two dictionaries.
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 99, 'c': 4}
merged_dict = dict1 | dict2
print(merged_dict)


#Find key with highest value.
dict2 = {'b': 99, 'c': 4,
         'd':87, 'e':56}
d=max(dict2)
print(d)


#Check if key exists.
user_profile = {"username": "johndoe", "email": "john@example.com"}
if "username" in user_profile:
    print("The 'username' key exists!")

if "age" not in user_profile:
    print("The 'age' key is missing.")


#Sort dictionary by values.
dict2 = {'g': 99, 'c': 4,
         'd':87, 'h':56}
p=sorted(dict2)
print(p)


#Create phonebook application.
phonebook = {}
while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add/Update Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == '1':
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        
        phonebook[name] = phone  
        print(f"Contact '{name}' saved successfully!")
      
    elif choice == '2':
        name = input("Enter name to search: ").strip()
        
        if name in phonebook:
            print(f"Found: {name} -> {phonebook[name]}")
        else:
            print("Error: Contact not found.")

    elif choice == '3':
        name = input("Enter name to delete: ").strip()
        
        if name in phonebook:
            del phonebook[name]
            print(f"Success: '{name}' has been deleted.")
        else:
            print("Error: Contact not found.")

    elif choice == '4':
        if len(phonebook) == 0:
            print("The phonebook is currently empty.")
        else:
            print("\n--- All Stored Contacts ---")
            for name, phone in phonebook.items():
                print(f"Name: {name} | Phone: {phone}")
    
    elif choice == '5':
        print("Exiting application. Goodbye!")
        break  # Stops the while loop
        
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")

        
#Word frequency counter.
text=input("enter a text:")
words = text.split()
wordcount={}
for word in words:
    if word in wordcount:
        wordcount[word]+=1
    else:
        wordcount[word]=1
print("word frequencies:")
for word, count in wordcount.items():
    print(f"{word}: {count}")
