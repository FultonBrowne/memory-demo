# code to demonstrate the python stack

def some_addition():
    print("deep stack")
    return 5 + 12

def some_subtraction():
    return 57 - some_addition()

def some_multiplication():
    return 23 * some_subtraction()

def some_division():
    return some_multiplication() / 2

def some_exponentiation():
    return some_division() ** 3

def some_modulo():
    t =  some_exponentiation() % 1232
    return t

def main():
    print(some_exponentiation())

main()