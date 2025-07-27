import random
import json

with open("quotes.json","r") as file:
    quotes=json.load(file)

def display():
    display_quote=random.choice(quotes)
    print(f'"{display_quote["quote"]}" - {display_quote["author"]}')

print("-----Quote Generator-----")
print("Press (q) to start")
while True:
    print("Press (y) for again\nPress (e) for exit")

    user_input = input()
    if user_input == 'q':
        
        display()
        
    elif user_input == 'y':
       
        display()

    elif user_input == 'e':
        
        print("Goodbye!")
        break

    else:
        
        print("Only (q), (y), and (e) are valid options. Please try again.")