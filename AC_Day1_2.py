#Day1
#Puzzle2

#translating numbers as words into their numbers
#use example line
#idea: use dictionary

#line = 'two1nine'
#word_to_number = {'one':'1', 'two':'2', 'three':'3',
#                  'four':'4', 'five':'5', 'six':'6', 'seven':'7',
#                 'eight':'8', 'nine':'9'}

#for word, digit in word_to_number.items():
#    line = line.replace(word, digit)

#print(line)

#now trying the same with many lines
#output
#219        29
#823        83
#abc123xyz  13
#x2134      24
#49872      42
#z18234     14
#7pqrst6    76

#one
#two
#three
#four
#five
#six
#seven
#eight
#nine

#overlapping possibilities
#twoone
#oneight
#threeight
#fiveight
#nineight
#eightwo
#eighthree
#sevenine
#added these to the dictionary

#lines = '''two1nine
#eightwothree
#abcone2threexyz
#xtwone3four
#4nineeightseven2
#zoneight234
#7pqrstsixteen'''

#lines_list = lines.splitlines()
#print(lines_list)

word_to_number = {'oneight':'18', 'threeight':'38', 'fiveight':'58',
                  'nineight':'98', 'eightwo':'82', 'eighthree':'83',
                  'sevenine':'79', 'twone':'21', 'one':'1', 'two':'2',
                  'three':'3', 'four':'4', 'five':'5', 'six':'6',
                  'seven':'7', 'eight':'8', 'nine':'9'}

for word, digit in word_to_number.items():
    line = input_string.replace(word, digit)

#print(line)

#rest should be the same as first puzzle

#put string into list of strings
lines_list = line.splitlines()
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
