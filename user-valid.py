#Username with <= 12 characters
#Username without spaces
#Username without digis

username = input("Enter a username: ")

if len(username) > 12:
    print("Username too long")

elif not username.find(" ") == -1:
    print("Username can't contain spaces")

elif not username.isalpha():
    print("Username can't contain digits")

else:
    print("Username valid")
    print("Welcome " ,username)