from utils.input_parser import txt_to_list

INPUT_PATH = "./input"
SAMPLE_PATH = "./sample"

RPS_DICT = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

SCORE_DICT = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 0,
    'Y': 3,
    'Z': 6,
}

def get_game_score(play, opp_play):
    if play == opp_play:
        return 3
    if play == 'A' and opp_play == 'B':
        return 0
    elif play == 'B' and opp_play == 'C':
        return 0
    elif play == 'C' and opp_play == 'A':
        return 0
    else:
        return 6

def get_move(opp_play, game_result):
    moves = ['A', 'B', 'C']

    if game_result == 'X':
        return moves[(moves.index(opp_play) - 1) % 3]
    elif game_result == 'Y':
        return opp_play
    elif game_result == 'Z':
        return moves[(moves.index(opp_play) + 1) % 3]

def calculate_total_score(input):
    total_score = 0

    for game in input:
        play_split = game.strip().split(' ')
        print(play_split)
        opp_play = play_split[0]
        game_result = play_split[1]
        game_score = SCORE_DICT[game_result]
        move_score = SCORE_DICT[get_move(opp_play, game_result)]
        total_score += (game_score + move_score)

    return total_score

def calculate_total_score_old(input):
    total_score = 0

    for game in input:
        play_split = game.strip().split(' ')
        print(play_split)
        opp_play = play_split[0]
        my_play = RPS_DICT[play_split[1]]
        game_score = get_game_score(my_play, opp_play)
        move_score = SCORE_DICT[my_play]
        total_score += (game_score + move_score)

    return total_score


if __name__ == '__main__':
    print(calculate_total_score(txt_to_list(INPUT_PATH)))
