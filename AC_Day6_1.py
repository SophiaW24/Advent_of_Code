#given: list of times & list of times
#want: product of #ways we beat record for all races -> four parts

#calculating product
#ways = [w1, w2, ..., wx]
#product = 1
#for number in ways:
#       product = number * product


#race_time = 7 ms
#record = 9 mm
#bpt + tt = race_time
#speed = bpt
#dist_travel > record
#speed * tt = dist
#for bpt in range(race_time):
#       tt = ~
#       speed = ~
#       dist = ~


#first step
#input file
#formating file
#we want to strings of race_time & record

file_path = 'Text_Day6.txt'

with open(file_path, 'r') as file:
    input_string = file.read()
#print(input_string)
#type(input_string) -> str

#make input string into list
input_list = input_string.split()
#type(input_list)

#split list in half
record = input_list[len(input_list)//2:]
race_time = input_list[:len(input_list)//2]
#print(time_list)
#print(distance_list)

#delete first element of list
race_time.pop(0)
#print(time_list)
record.pop(0)
#print(distance_list)


# Convert each element from string to integer
race_time = [int(time) for time in race_time]
record = [int(number) for number in record]
#print(race_time)
#print(record)

#solving one race
def win_race(race_time, record):
    wins = 0
    for bpt in range(race_time):
        tt = race_time - bpt    #travel time
        speed = bpt             #bpt = button press time
        dist = tt * speed       #distance
        if dist > record:
            wins += 1
        else:
            continue

    return wins                 #works!

#call function with
#win_race(7, 9)

#solving many races
#race_time = [7, 15, 30]
#record = [9, 40, 200]
amount_of_wins = []

#for time in race_time:
#    for number in record:
#        wins = win_race(time, number)
#        if wins > 0:
#            amount_of_wins.append(wins)
#print(amount_of_wins)

for time, number in zip(race_time, record):
    wins = win_race(time, number)
    if wins > 0:
        amount_of_wins.append(wins)
#print(amount_of_wins)

# Multiply all numbers in the list
# Initialize product to 1
product = 1
for numbers in amount_of_wins:
    product *= numbers

print(product)
