file_path = 'Text_Day9.txt'

with open(file_path, 'r') as file:
    input_lines = file.read().split('\n')
    #print(type(input_lines))


def predict_next(num):
    next_num = []
    #print(num)
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
        #if row of numbers is not the same yet, recurse until it is
        b = int(num[-1]) + predict_next(next_num)
        #print(b)
        return b


def read_all_lines(data):
    pred_per_line = []
    #avoiding split is not for list error
    for line in data:
        if type(line) == str:
            num = line.split()
        else:
            num = line
        #predict next number of each line
        diff = predict_next(num)
        #add predictions to list
        pred_per_line.append(diff)

    total_sum = sum(pred_per_line)
    return total_sum

print(read_all_lines(input_lines))