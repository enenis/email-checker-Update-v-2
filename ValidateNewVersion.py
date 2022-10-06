email = input("What's your email: ").strip()

username,domain=email.split("@")

try:
    if username and domain.endswith(".edu"):
        print("valid")
    elif username and domain.endswith(".com"):
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("Wrong mail")