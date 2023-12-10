#function to check if game is valid
#input is dictionary with ids & game rounds and max values for each color as dictionary
def game_validation(games, maximum_values):
    #save ids of possible games
    possible_games = []

    #loop through keys and values of games dictionary
    for game_id, game_rounds in games.items():
        #start counter for each color
        red, green, blue = 0, 0, 0
        #loop through each round of each game
        for game_round in game_rounds:
            #print(game_round)
            #loop through each color with number of each round and each game, split by , 
            for cubes in game_round.split(','):
                #print(cubes)
                #save count and color of cubes; strip removes empty spaces; split splits with empty spaces between numbers or words
                count, color = cubes.strip().split()
                #save max count of each color of one game total
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
        #if saved count is below then allowed count, its id will be saved in list
        if red <= maximum_values['red'] and green <= maximum_values['green'] and blue <= maximum_values['blue']:
            possible_games.append(int(game_id))
    return possible_games


def main():
    file_path = 'Text_Day2.txt'
    #make dictionary for ids and all rounds of each game
    games = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            #create two parts that are divided by :
            parts = line.split(':')
            #save first part of parts as id -> split again at empty space and save second part, so you only have number as id
            ID = parts[0].split()[1]
            #print(ID, parts[1])
            rounds = []
            #save second part of parts (rounds of each game) and split them with ; -> you get list of each rounds as strings together
            for round in parts[1].strip().split(';'):
                rounds.append(round)
            #print(rounds)
            #fill dictionary that was created at the beginning -> IDs are keys and rounds are values (anything can be appended as value like strings or lists or dicts, etc.)
            games[ID] = rounds
    #print(games)

    maximum_values = {'red':12, 'green':13, 'blue':14}
    #call function:
    valid_ids = game_validation(games, maximum_values)
    #print(valid_ids)
    #f in the beginning let´s you put a variable inside a written string -> nice for aesthetics
    print(f'Sum of game ids: {sum(valid_ids)}')

#call function
main()