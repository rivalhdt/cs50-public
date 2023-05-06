def main():
    prompt = input("Expression: ")
    x, y, z = prompt.split(" ")
    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(plus(x,z))
        case "-":
            print(subs(x,z))
        case "*":
            print(mult(x,z))
        case "/":
            print(div(x,z))

def plus(n1, n2):
    return n1 + n2

def subs(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

main()