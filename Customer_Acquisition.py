import requests

SHEETY_USER_ENDPOINT = ""

# Post customers' data to google sheet via Sheety
def update_info(fname,lname,email):

    new_data = {"user": {"firstName": fname, "lastName": lname, "email": email}}
    print(new_data)
    requests.post(url=f"{SHEETY_USER_ENDPOINT}", json=new_data)

print("Welcom to Flight Club.\nWe find the best flight deals and email you.")
email='gmail'
email_confirm='hotmail'
fname=input("What is your first name?\n")
lname=input("What is your last name?\n")
if email != email_confirm:
    email=input("What is your email?\n")
    email_confirm=input("Type your email again.\n")
update_info(fname,lname,email)
print("You're in the club!")


