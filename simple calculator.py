print("=== Simple Calculator ===")
print("press 'q' to quit.\n")

op=""#intialise so loop runs at least once
while op !="q":
    op=input("enter operation(+,-,*,/ or q to quit):")
    
    if op == "q": #user wants to quit
        print("\nExiting...Goodbye!\n")
        break
    if op not in ('+','-','*','/'):
        print("invalid operator! Try again.\n")
        continue
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if op == '+':
        print((a,b))
    
        
    
    
    
    