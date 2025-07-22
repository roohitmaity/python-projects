# importing random module
import random
# basic setup
print("----Password Generator 4-digit----")
print("Provide Range(ex.0-9)")
a=int(input("Start\t"))
z=int(input("End\t"))
# validation of end range
if z>9:
    print("prodvide upto 9 only")
    exit()
breakpoint
# temporary variable
p=""
# actual loop with random function
for i in range(4):
    digits=random.randrange(a,z)
    p+=str(digits)
# printing the password
print(f"Your Password: {p}")