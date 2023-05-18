# smurf on those elementary school kids
import math

text = open("demo.txt", "r").readlines()
howMany = text[0]

for x in range(1, int(howMany) + 1):
    info = text[x].split(" ")
    operator = info[0]
    a = int(info[1])
    b = int(info[2])

    if operator == "add":
        print(a + b)
    if operator == "sub":
        print(a - b)
    if operator == "mul":
        print(a * b)
    if operator == "rem":
        print(a % b)
    if operator == "min":
        print(min(a, b))
    if operator == "max":
        print(max(a, b))
    if operator == "gcd":
        print(math.gcd(a, b))
    if operator == "lcm":
        print(math.lcm(a, b))
    if operator == "dif":
        print(abs(a - b))