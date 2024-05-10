import sys

def pretty_print(table):
    for i in range(len(table)):
        print(table[i])


# def recursive_make_change(table, quantities, amounts, cents):
#     if cents <= 0:
#         return 0
    
#     if table[cents] != sys.maxsize:
#         return table[cents]
    
#     total = sys.maxsize
#     # for i in range (cents):
#     for j in range (len(quantities)):
#         if quantities[j] > 0:
#             new_cents = cents - amounts[j]
#             quantities[j] -= 1
#             print (j, quantities, new_cents)
#             min_coins = min(total, recursive_make_change(table, quantities, amounts, new_cents)) + 1
#     print("call on:", cents, min_coins)
#     table[cents] = min_coins
#     return min_coins

    # if cents <= 0:
    #     return 0
    
    # total = sys.maxsize
    # for i in range(len(quantities)):
    #     print(i)
    #     if quantities[i] > 0:
    #         new_cents = cents - amounts[coin]
    #         quantities[i] -= 1
    #         min_coins = min(total, recursive_make_change(table, quantities, amounts, cents, i, quantities[i])) + 1
    # table[coin][quantity][0] = min_coins
    # return min_coins



def iterative_make_change(table, quantities, amounts, cents):
    if cents == 0:
        return 0
    
    # if table[cents] != sys.maxsize:
    #     return table[cents]
    
    coin = 0
    last_stop = 0
    print(table[0])
    for i in range (1, cents + 1):
        cur_coins = sys.maxsize
        for j in range(3, -1, -1):
            # print("here1", table[i][1][j])
            if table[i][1][j] > 0:
                # print("here2", table[i][1])
                if i - amounts[j] >= 0:
                    if table[i - amounts[j]][0] != sys.maxsize and table[i - amounts[j]][1][j] != 0:
                        # print("here4")
                        round_coins = table[i - amounts[j]][0] + 1
                        if round_coins < cur_coins:
                            cur_coins = round_coins
                            coin = j
                            last_stop = i - amounts[j]
                            # print("here5", round_coins, coin, last_stop)
        table[i][0] = cur_coins
        # print(table[last_stop])
        table[i][1] = table[last_stop][1].copy()
        table[i][1][coin] -= 1
        print(i, table[i])
    
    print(table)
    if table[-1][0] != sys.maxsize:
        print(table[-1][0])
    else:
        if all(v == 0 for v in table[-1][1]):
            print ("IOU")
        else:
            min = table[-1][0]
            for j in range(len(quantities)):
                start = len(table) - 1 - amounts[j]
                for i in range(start, len(table)):
                    if table[i][1][j] > 0:
                        new_min = table[i][0]
                        if new_min < min:
                            min = new_min
                print(min + 1)
                return
            # print(table[-1][0] + 1)
            print("here")


def make_change(cents, quantities):
    table = []
    table.append([0, quantities[:]])
    for i in range(cents):
        table.append([sys.maxsize, quantities[:]])
    # print (table)
    # table = []
    # quant = len(quantities)
    # for i in range(len(quantities)):
    #     line = []
    #     for j in range(quantities[i]):
    #         line.append((sys.maxsize, cents))
    #     table.append(line)
    # pretty_print(table)

    # amount = 3
    amounts = [25, 10, 5, 1]
    iterative_make_change(table, quantities, amounts, cents)
    # print(coins)


def main():
    # cents = int(input())
    # quantities = [int(x) for x in sys.stdin.readline().split()]
    # cents = 59
    # quantities = [2, 3, 0, 9]
    cents = 45
    quantities = [2, 1, 1, 3]
    # cents = 90
    # quantities = [2, 2, 2, 2]
    print(cents, quantities)
    make_change(cents, quantities)

if __name__ == "__main__":
    main()