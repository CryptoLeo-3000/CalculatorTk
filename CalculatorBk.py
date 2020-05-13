import math
import random

def calculate(operation):
    first = operation[0]
    if first == "+" or first == "-" or first == "*" or first == "/":
        operation.insert(0, "0")

    l = len(operation)

    while len(operation) != 1:
        try:
            if operation[1] == "+":
                final = float(operation[0]) + float(operation[2])
                operation.pop(0)
                operation.pop(0)
                operation.pop(0)
                operation.insert(0, str(final))
            elif operation[1] == "-":
                final = float(operation[0]) - float(operation[2])
                operation.pop(0)
                operation.pop(0)
                operation.pop(0)
                operation.insert(0, str(final))
            elif operation[1] == "*":
                final = float(operation[0]) * float(operation[2])
                operation.pop(0)
                operation.pop(0)
                operation.pop(0)
                operation.insert(0, str(final))
            elif operation[1] == "/":
                final = float(operation[0]) / float(operation[2])
                operation.pop(0)
                operation.pop(0)
                operation.pop(0)
                operation.insert(0, str(final))
        except:
            pass

    return operation