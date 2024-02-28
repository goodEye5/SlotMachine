import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
symbol_count = {
    "A":3,
    "B":6,
    "C":9,
    "D":10
}
symbol_value = {
    "A":4,
    "B":3,
    "C":2,
    "D":1
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_line.append(line+1)
    return winnings,winning_line
def spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
def deposit():
    balance = 0
    while True:
        amount = input("Deposit amount: ")
        try:
            amount = int(amount)
            balance = balance + amount
            print("New balance: {}$".format(balance))
            break
        except ValueError:
            print("Enter a valid number")
            pass
    return balance
def get_lines():
    while True:
        lines = input("Line amount (1-{}): ".format(MAX_LINES))
        try:
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Lines must be bewteen 1 and {}".format(MAX_LINES))
        except ValueError:
            print("Enter a number")
            pass
    return lines
def get_bet():
    while True:
        bet = input("Your bet ({}-{}): ".format(MAX_BET, MIN_BET))
        try:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet must be bewteen {} and {}".format(MAX_BET,MIN_BET))
        except ValueError:
            print("Enter a number")
            pass
    return bet
def game(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"""You cannot bet more than you possess.
    Your total bet attempt: {total_bet}.
    Your balance: {balance}.
    Selected lines {lines}.""")
        else:
            break
    print("-" * 50)
    print(f"""Your Bet: {bet}
    Lines: {lines}
    Total Bet: {total_bet}""")
    slots = spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}")
    print("Winning lines: ", *winning_line)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance: {balance}")
        answer = input("Press enter to spin or q to quit")
        if answer == "q":
            break
        balance += game(balance)


main()


