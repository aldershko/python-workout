import random

def play():
    user = input("What is your choice? 'r' for rock, 's' for scissors ,'p' for paper:\n")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return "Its a tie"
    
    if is_win(user,computer):
        return "You won"
    
    return 'you lost'


    #r>s,s>p,p>r





def is_win(player, opponent):
    if(player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())