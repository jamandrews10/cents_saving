import sys

def get_answer(table, quantities, amounts):
    """
    Checks the three cases for an answer

    Parameters
    ----------
    table : list of list of ints
        keeps track of coins used and remaining

    quantities : list of ints
        Number of each coin

    amounts : list of ints
        Value of each coin

    cents : int
        Total number of cents to reach
        
    """
    
    # if table has been fileld
    if table[-1][0] != sys.maxsize:
        print(table[-1][0])
    else:
        # if we are out of coins
        if all(v <= 0 for v in table[-1][1]):
            print ("IOU")
        else:
            min = table[-1][0]
            # find the largest coin remaining
            for j in range(len(quantities)):
                start = len(table) - 1 - amounts[j]
                # iterate from cents - amount to cents 
                for i in range(start, len(table)):
                    # find the lowest coin value and add one
                    if table[i][1][j] > 0:
                        new_min = table[i][0]
                        if new_min < min:
                            min = new_min
                print(min + 1)
                return

def iterative_make_change(table, quantities, amounts, cents):
    """
    Calculates the coins used at each cent value

    Parameters
    ----------
    table : list of list of ints
        keeps track of coins used and remaining

    quantities : list of ints
        Number of each coin

    amounts : list of ints
        Value of each coin

    cents : int
        Total number of cents to reach

    """

    # If no cents to make
    if cents == 0:
        print ("O")
        return
    
    coin = 0
    last_stop = 0
    # iterate over every value in list (all cents values)
    for i in range (1, cents + 1):
        cur_coins = sys.maxsize

        # iterate over all coin values, pennies to quarters
        for j in range(3, -1, -1):

            # if current cents - value of coin is above 0
            if i - amounts[j] >= 0:

                # if table at current cents - value has been adjusted, and there are coins left
                if table[i - amounts[j]][0] != sys.maxsize and table[i - amounts[j]][1][j] != 0:
                    round_coins = table[i - amounts[j]][0] + 1

                    # if we found a smaller number of coins
                    if round_coins < cur_coins:
                        cur_coins = round_coins
                        coin = j
                        last_stop = i - amounts[j]

        # update the table
        table[i][0] = cur_coins
        table[i][1] = table[last_stop][1].copy()
        table[i][1][coin] -= 1
    
    get_answer(table, quantities, amounts)

def make_change(cents, quantities):
    """
    Creates table and calls iterative function

    Parameters
    ----------
    cents : int
        Total number of cents to reach

    quantities : list of ints
        Number of each coin

    """

    # make a table of cents length that has the coins used and a list of coins remaining 
    table = []
    table.append([0, quantities[:]])
    for i in range(cents):
        table.append([sys.maxsize, quantities[:]])

    # values of coins
    amounts = [25, 10, 5, 1]
    iterative_make_change(table, quantities, amounts, cents)

def main():
    """
    Calls make change
    """
    cents = int(input())
    quantities = [int(x) for x in sys.stdin.readline().split()]
    make_change(cents, quantities)

if __name__ == "__main__":
    main()