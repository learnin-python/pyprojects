import re

print("Our magical calculator")
print("Type quit to exit\n")


previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))



    if equation == "quit":
        print("Goodbye, Human")
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("You typed", equation)
while run:
    performMath()
