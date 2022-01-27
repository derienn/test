import sys
import pprint
import random

lines = []
number = 11

for i in range(number):
    lines.append(f'{i+1}. line')

with open("pa_lines.txt", mode="w", encoding="UTF-8") as k:
    for line in lines:
        k.write(line + '\n')

with open("pa_lines.txt", mode="r", encoding="UTF-8") as file:
    file_data = file.read()
    print(file_data , end = "")
    # number_of_lines = file_data.count('\n')

print(f'A sum of {number} lines found in the pa_lines.txt file')