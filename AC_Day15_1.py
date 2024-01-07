file_path = 'Text_Day15.txt'

with open(file_path, 'r') as file:
        for line in file:
                #print(line)
                strings = line.strip().split(',')
#print(strings)

test_data = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'.split(',')
t2 = 'HASH'
points = 0
for string in strings:
        value_letter = 0
        for letter in string:
                value_letter += ord(letter)
                value_letter *= 17
                value_letter %= 256
        points += value_letter

print(points)