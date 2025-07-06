person = {"name": "Ali", "age": 25, "city": "Tashkent"}

user_asked = input()

if user_asked in person:
    print(person.pop(user_asked))
    print(person)  
else:
    print('404 not found') 