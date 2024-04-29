import sys

def rounding(price):
    leftover = price % 10 
    if leftover > 4:
        price = price + (10 - leftover)
    else:
        price = price - leftover 
    return price



def recursive_ents(table, start, dividers, prices, last_divide):
    total = 0
    if table[dividers][start] != sys.maxsize:
        return table[dividers][start]

    if start == len(prices) or dividers == 0:
        total = rounding(sum(prices[last_divide:]))
        table[dividers][len(prices)] = total
        # print("dividers: ", dividers, "items: ", items, "total: ", total)
        return total
    
    total = sys.maxsize
    usedivide = 0
    dontdivide = 0
    for i in range(start, len(prices)):
        usedivide = recursive_cents(table, i, dividers - 1, prices, i) + rounding(sum(prices[last_divide:i]))
        dontdivide = recursive_cents(table, i + 1, dividers, prices, last_divide)
        total = min(total, usedivide, dontdivide)
        total = rounding(total)
        table[dividers][i] = total
        # print("dividers: ", dividers, "items: ", i, "total: ", total)
    return total

# def recursive_cents(table, items, dividers, prices, last_divide):

#     total = 0
#     # print(dividers, items)
#     if table[dividers][items] != sys.maxsize:
#         return table[dividers][items]
    
#     if items == 0 or dividers == 0:
#         total = rounding(sum(prices[:last_divide]))
#         table[dividers][items] = total
#         print("dividers left: ", dividers, "items: ", items, "total: ", total)
#         return total
     
#     total = sys.maxsize
#     usedivide = 0
#     dontdivide = 0
#     for i in range(items, -1, -1):
#         usedivide = recursive_cents(table, i - 1, dividers - 1, prices, i) + rounding(sum(prices[i:last_divide]))
#         dontdivide = recursive_cents(table, i - 1 , dividers, prices, last_divide)
#         total = min(total, usedivide, dontdivide)
#         total = rounding(total)
#         table[dividers][i] = total
#         print("dividers left: ", dividers, "items: ", i, "total: ", total)
#     return total

def recursive_cents(table, items, dividers, prices, last_divide):

    total = 0
    # print(dividers, items)
    if table[dividers][items] != sys.maxsize:
        return table[dividers][items]
    
    if items == 0 or (dividers == 0 and items >= 1):
        total = rounding(sum(prices[last_divide :]))
        table[dividers][items] = total
        # print("dividers left: ", dividers, "items: ", items, "total: ", total)
        # pretty_print(table)
        return total
     
    total = sys.maxsize
    usedivide = 0
    dontdivide = 0
    for i in range(items, -1, -1):
        dontdivide = recursive_cents(table, i - 1 , dividers, prices, last_divide)
        usedivide = recursive_cents(table, i - 1, dividers - 1, prices, i) + rounding(sum(prices[last_divide : i]))
        total = min(total, usedivide, dontdivide)
        total = rounding(total)
        table[dividers][i] = total
        # print("dividers left: ", dividers, "items: ", i, "total: ", total)
        # pretty_print(table)
    return total



def pretty_print(table):
    for i in range(len(table)):
        print(table[i])

def cents(items, dividers, prices):
    table = []
    for i in range(dividers + 1):
        line = []
        for j in range(items + 1):
            line.append(sys.maxsize)
        table.append(line)

    cost = recursive_cents(table, items, dividers, prices, 0)
    # cost = recursive_cents(table, 0, dividers, prices, 0)
    # print()
    # pretty_print(table)
    # print()
    print (cost)

def main():
    items, dividers  = map(int, input().split())
    prices = [int(x) for x in sys.stdin.readline().split()]
    cents(items, dividers, prices)

if __name__ == "__main__":
    main()