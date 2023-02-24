import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}



def check_winnings(lines,bet,columns,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines

def get_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    #what we will get after this loop is columns = [[a,b,c],[b,d,a],[c,b,d]]

    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

#in this function we will flip the rows and make the columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print() #here print is used to bring the rows to the next line
    

def deposit():
    while True:
        amount = input("Please enter the amount you want to deposit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit an amount greater than zero")
        else:
            print("Please enter a digit")
    return amount
    
def get_number_of_lines():
    while True:
        lines = input(" Enter the number of lines you want to bet from (1 - " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a line in given range")
        else:
            print("Please enter a valid line")
    return lines

def get_bet():
    while True:
        bet = input(" What would you like to bet? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a bet amount in given range ({MIN_BET} - {MAX_BET})")
        else:
            print("Please enter a valid bet amount")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet  = get_bet()
        total_bet  = bet * lines
        if total_bet > balance:
            print(f"Sorry you dont have enough balance to bet on. Your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is : {total_bet}")

    slot  = get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winnings,winning_lines = check_winnings(lines,bet,slot,symbol_value)
    print(f"You have won: {winnings}")
    print(f"Your winnings lines are {winning_lines}")

    return winnings - total_bet



def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or (q to quit)")

        if answer == 'q':
            break
        balance += spin(balance)

    print(f"YOu are left with ${balance}") 
    


main()
