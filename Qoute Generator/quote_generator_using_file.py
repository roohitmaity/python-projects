import random
import json

with open(r"C:\Users\ethic\Desktop\python projects\Qoute Generator\quotes.json","r") as file:
    quotes=json.load(file)

def display():
    display_quote=random.choice(quotes)
    print(f'"{display_quote["quote"]}" - {display_quote["author"]}')

print("-----Quote Generator-----")
print("Press (q) to start")
while True:
    print("Press (y) for again\nPress (e) for exit")

    user_input = input().lower()
    if user_input == 'q':
        # Show the first quote when 'q' is pressed
        display()
        
    elif user_input == 'y':
        # Show another quote when 'y' is pressed
        display()

    elif user_input == 'e':
        # Exit the program when 'e' is pressed
        print("Goodbye!")
        break

    else:
        # Handle invalid input
        print("Only (q), (y), and (e) are valid options. Please try again.")