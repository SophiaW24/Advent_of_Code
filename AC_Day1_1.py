#Day 1
#Puzzle 1

#retrieve a specific calibration number
#given:
    #code (alphanumeric)
    #first & last digit, form 2-digit number
    #we want the sum of all 2-digit numbers

#for every line of code
    #read first, last digit
    #form 2-digit number
#sum

#code for one line string
#line = '1abc2'
#number = ''
#for i in range(len(line)):
#    if line[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#        number += line[i]
#print(number)

#tried to use function but couldn´t quite figure it out
#but just printing the code in python worked!
#def calibration(input_string):

#put string into list of strings
lines_list = input_string.splitlines()
#put all numbers into list
numbers = []

#loop through the list
for i in lines_list:
    #numbers of each line as string (append later to list)
    line_numbers = ''
    #loop through each string of the list
    for j in i:
        #if programm fins a digit from 0-9
        if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            #add it to string
            line_numbers += j
    #then append string to list
    #this way it will safe the numbers as string in a list and not each single number in a list
    numbers.append(line_numbers)

print(numbers)

#idea
#all digits that are > 2, take first and last digit and make new number
#if digit == len(1) add same digit to it
#print all 2-digit numbers

#store new numbers here
digits = []

#loop through each number of the list
for i in numbers:
    #check if length of number equals 2
    if len(i) == 2:
        #append if true
        digits.append(i)
    #check if length of number is > 2    
    elif len(i) > 2:
        #if true, take first and last digits to create new number
        new_number = i[0] + i[-1]
        #append new number
        digits.append(new_number)
    #check if length of number equals 1
    elif len(i) == 1:
        #if true append same number to it
        digits.append(i + i)

print(digits)

#convert strings to intergers, otherwise sum function doesn´t work
#sum all numbers in list digits to get final result

digits_int = [int(digit) for digit in digits] #Googled this
print(digits_int)
result = sum(digits_int)

print(result)

#print this first into python
#then all of the above
file_path = 'Text_Day1_Puzzle1.txt'

with open(file_path, 'r') as file:
    input_string = file.read()

#final_result = calibration(input_string)
#print(finalresult)
