import sys

def rounding(price):
    leftover = price % 10 
    if leftover > 4:
        price = price + (10 - leftover)
    else:
        price = price - leftover 
    return price


def recursive_cents(table, items, dividers, prices, last_divide):

    total = 0
    # print(dividers, items)
    if table[dividers][items] != sys.maxsize:
        return table[dividers][items]
    
    if items == 0 or dividers == 0:
        total = rounding(sum(prices[:last_divide]))
        table[dividers][items] = total
        # table[i] = total
        return total
     
    total = sys.maxsize
    usedivide = 0
    dontdivide = 0
    for i in range(items - 1 , -1, -1):
        usedivide = recursive_cents(table, items - 1, dividers - 1, prices, i) + rounding(sum(prices[i:last_divide]))
        dontdivide = recursive_cents(table, items -1 , dividers, prices, last_divide)
        total = min(total, usedivide, dontdivide)
        total = rounding(total)
        table[dividers][i] = total
        # table[i] = total
    return total

def cents(items, dividers, prices):
    

    table = []
    for i in range(dividers + 1):
        line = []
        for j in range(items + 1):
            line.append(sys.maxsize)
        table.append(line)


    # table = [sys.maxsize] * items

    # print (table)
    cost = recursive_cents(table, items, dividers, prices, items)
    # print(table)
    print (cost)

def main():
    items, dividers  = map(int, input().split())
    prices = [int(x) for x in sys.stdin.readline().split()]
    # print (items)
    # print(dividers)
    # print (prices)
    cents(items, dividers, prices)

if __name__ == "__main__":
    main()