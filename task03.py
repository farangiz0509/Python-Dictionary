users = []
for i in range(2):
    name = input("enter the name :")
    email = input("enter the  email")

    user = { 'name': name,'email': email}
    users.append(user)


print(users)