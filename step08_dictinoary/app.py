# simple example
userinfo = {
    "username": "tanoli",
    "password": 1234,
    "email": "sharjeeel3@gmail.com"
}
print(userinfo["username"])

# updating the value of username
userinfo["username"] = "sharjeel"

print(userinfo["username"])

# adding a new key-value pair
userinfo["age"] = 25

print(userinfo)

# checking if a key exists in the dictionary
print(userinfo.get("email", "Email not found"))

# removing a key-value
del userinfo["email"]
print(userinfo)

userinfo2 = {
    "username": "khan",
    "password": 1034,
    "email": "sharjeeel4@gmail.com"
}

# dictionary in list
users = [userinfo, userinfo2]
print(users)