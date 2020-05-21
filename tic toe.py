def draw_board(char_list):
    print("\n\tTic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + char_list[0] + " || " + char_list[1] + " || "+ char_list[2] + " ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + char_list[3] + " || " + char_list[4] + " || " + char_list[5]+ " ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print("\t|| " + char_list[6] + " || " + char_list[7] + " || "+  char_list[8]+ " ||")
    print("\t~~~~~~~~~~~~~~~~~")

def get_player_input(player_move,char_list):
    while True:
        user_input=int(input("Enter a place:(1-9)"))
        if user_input > 0 and user_input <= 9:
            if char_list[user_input-1]=="_":
                return user_input
            else:
                print("spot is not empty")
        else:
            print("It doesnt exists. Enter between (1-9) ")

def place_char_on_board(player_char,player_move,char_list):
    char_list[player_move-1]=player_char

def is_winner(char_list,player_char):
            #row
    return ((char_list[0]==player_char and char_list[1]==player_char and char_list[2]==player_char) or
            (char_list[3]==player_char and char_list[4]==player_char and char_list[5]==player_char) or
            (char_list[6]==player_char and char_list[7]==player_char and char_list[8]==player_char) or
           #diagonal
            (char_list[0]==player_char and char_list[4]==player_char and char_list[8]==player_char) or
            (char_list[2]==player_char and char_list[4]==player_char and char_list[6]==player_char) or
            #column
            (char_list[0]==player_char and char_list[3]==player_char and char_list[6]==player_char) or
            (char_list[1]==player_char and char_list[4]==player_char and char_list[7]==player_char) or
            (char_list[2]==player_char and char_list[5]==player_char and char_list[8]==player_char))
player_1="x"
player_2="o"
c_list=['_']*9
draw_board(c_list)
while True:
    move=get_player_input(player_1,c_list)
    place_char_on_board(player_1,move,c_list)
    draw_board(c_list)
    if is_winner(c_list,player_1):
        print("player 1 wins")
        break
    #chk for tie
    elif "_" not in c_list:
        print("tie")
        break

    move = get_player_input(player_2, c_list)
    place_char_on_board(player_2, move, c_list)
    draw_board(c_list)
    if is_winner(c_list, player_2):
        print("player 2 wins")
        break
    # chk for tie
    elif "_" not in c_list:
        print("tie")
        break
