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


# Convert each number to a string and concatenate them (making one number)
one_time = int(''.join(map(str, race_time)))
one_record = int(''.join(map(str, record)))
print(one_time)
print(one_record)

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
win_race(one_time, one_record)
