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
    if items == 0 or dividers == 0:
        total = rounding(sum(prices[:last_divide]))
        table[items] = total
        return total
     
    total = sys.maxsize
    usedivide = 0
    dontdivide = 0
    for i in range(items - 1 , -1, -1):
        usedivide = recursive_cents(table, items - 1, dividers - 1, prices, i) + rounding(sum(prices[i:last_divide]))
        dontdivide = recursive_cents(table, items - 1, dividers, prices, last_divide + 1)
        total = min(total, usedivide, dontdivide)
        total = rounding(total)
        table[i] = total
    return total

def cents(items, dividers, prices):
    table = [sys.maxsize] * items

    print (table)
    cost = recursive_cents(table, items, dividers, prices, items)
    print(table)
    print (cost)

def main():
    # items = 3
    # dividers = 1
    # prices = [13, 21, 54]
    items = 5
    dividers = 2
    prices = [1, 1, 1, 1, 1]
    cents(items, dividers, prices)

main()