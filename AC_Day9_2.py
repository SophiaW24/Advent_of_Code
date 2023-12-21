file_path = 'Text_Day9.txt'

with open(file_path, 'r') as file:
    input_lines = file.read().split('\n')
    #print(type(input_lines))


def predict_next(num):
    next_num = []
    for i in range(len(num)):
        #avoid list index out of range error
        if i > 0:
            next_num.append(int(num[i]) - int(num[i-1]))
    
    #set = store multiple items in a single variable
    if len(set(next_num)) == 1:
        a = int(num[-1]) + int(next_num[0])
        #print(a)
        return a
    else:
        #print(num[-1])
        b = int(num[-1]) + predict_next(next_num)
        #print(b)
        return b

#print(predict_next(value))


def read_all_lines(data):
    diff_per_line = []
    for line in data:
        if type(line) == str:
            num = line.split()
        else:
            num = line
        #reverse row when putting into predict_next function! -> gives you first predictions
        diff = predict_next(num[::-1])
        diff_per_line.append(diff)

    total_sum = sum(diff_per_line)
    return total_sum

print(read_all_lines(input_lines))