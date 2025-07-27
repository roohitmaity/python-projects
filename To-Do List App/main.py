print("--------TO-DO List App--------")

while True:
    cmd=int(input('''
    Press 0 to exit task app. 
    Press 1 to add task.
    Press 2 to list task.\n\n
    Your Choice : '''))

    if cmd==1:
        with open("data.txt",'a')as file:
            while True:
                task=input("Write your tasks when you done just write 'done' : ")
                if task.lower()=='done':
                    break
                file.write(task+"\n")
                print("Task added")
    elif cmd==2:
        print("-------Your Tasks----------")
        try:
            with open("data.txt",'r')as file:
                content=file.read()
                if content.strip()=="":
                    print("No Entries !!!")
                else:
                    print(content)
        except FileNotFoundError:
            print("no file exists !")
    elif cmd==0:
        print("bye bro !")
        break
    else:
        print("invalid command")         
    
        

