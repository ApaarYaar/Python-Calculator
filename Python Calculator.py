import re

print("Python Calculator")
print("Type 'restart' to Refresh")
print("Type 'quit' to Exit")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Good Bye! See You Next Time...")
        run = False
    elif equation == 'restart':
        previous = 0
    else:
        equation = re.sub('[a-zA-Z,;:"@?#$&()]', '', equation)
        if len(equation) <= 0:
            print("Enter valid equation!")
            return

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("Solution:", previous)


while run:
    perform_math()
