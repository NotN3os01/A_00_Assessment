import math
import random



num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
symbol_list = ('*', '+', '/', '-')
comp_choice = random.choice(symbol_list)


z = comp_choice
x = num1
y = num2
answer = eval(f"{x} {z} {y}")


