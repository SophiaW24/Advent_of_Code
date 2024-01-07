file_path = 'Text_Day4.txt'
lines = []

with open(file_path, 'r') as file:
        for line in file:
                #print(line)
                sep_ID_num = line.strip().split(':')
                #print(sep_ID_num)
                left_right_num = sep_ID_num[1]
                #print(left_right_num)                   #each line a string
                lines.append(left_right_num)

#print(lines)
total_sum = 0
for i in lines:
        line = i.split('|')
        #print(line)
        win = list(map(int, line[0].split()))
        #print(win)
        have = list(map(int, line[1].split()))
        #print(have)
        same_num = list(set(win) & set(have))               #find same numbers
        #print(same_num)
        points = 0
        num_matches = len(same_num)
        if num_matches > 0:
                points += 1
                num_matches -= 1
                while num_matches > 0:
                        points = points * 2
                        num_matches -= 1
                total_sum += points
print(total_sum)