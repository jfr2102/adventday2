from sampleInput import *
input_split = Sampleinput.split()
input_formated = list(zip(*(iter(input_split),) * 3))

correct_count = 0

for rule,char,pwd in input_formated:
    min = int(rule.split("-")[0])
    max = int(rule.split("-")[1])
    char = char[0]
    occur = pwd.count(char)
    if occur <= max and occur >= min:
        correct_count += 1
print(correct_count, "of", len(input_formated), "passwords are correct.")