#part 2 of Day 2 is the same except:
#deleted part where numbers are compared to maximum values
#you just want min possible number of cube
#the code already saves the highest cube number of each game as red, green and blue
#that´s why we just need to multiply it in the loop, so each game will be already multiplied
#then the result will be added to sum so all multiplied numbers will be automatically added up
#see changes at line 12, 32, 33 -> rest is the same, only changed variable number in line 57 for context


def game_validation(games, maximum_values):
    possible_games = []
    sum = 0

    for game_id, game_rounds in games.items():
        red, green, blue = 0, 0, 0
        for game_round in game_rounds:
            for cubes in game_round.split(','):
                #print(cubes)
                count, color = cubes.strip().split()
                if color == 'red':
                    if int(count) > red:
                        red = int(count)
                elif color == 'green':
                    if int(count) > green:
                        green = int(count)
                elif color == 'blue':
                    if int(count) > blue:
                        blue = int(count)
                else:
                    print('invalid color')
            #print(red, green, blue)
        sum += red * green * blue 
    return sum
        
    
            #print(game_id, game_round)

def main():
    file_path = 'Text_Day2.txt'

    games = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(':')
            ID = parts[0].split()[1]
            #print(ID, parts[1])
            rounds = []
            for round in parts[1].strip().split(';'):
                rounds.append(round)
            #print(rounds)
            games[ID] = rounds
    #print(games)

    maximum_values = {'red':12, 'green':13, 'blue':14}
    #call function and save as variable:
    result = game_validation(games, maximum_values)
    #print(valid_ids)
    print(f'Sum of game ids: {result}')

#call function
main()