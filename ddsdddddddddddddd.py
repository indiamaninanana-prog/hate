a = float(input())
b = float(input())
op = input().strip()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print(a / b)