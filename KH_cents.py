#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:04:16 2024

@author: kaihaesslein
"""

import sys

def rounding(price):
    leftover = price % 10 
    if leftover > 4:
        price = price + (10 - leftover)
    else:
        price = price - leftover 
    return price


def non_recursive_cents(table, items, dividers, prices):

    total = sys.maxsize

    for d in range(0, dividers + 1):
        
        last_divide = 0

        for i in range(0, items + 1):
            if i == 0:
                print("ITEM BC")
                table[d][i] = 0
            elif d == 0:
                print("DIVIDE BC 1")
                table[d][i] = rounding(sum(prices[:i]))
            elif d >= i:
                print("DIVIDE BC 2")
                table[d][i] = table[d - 1][i]
                last_divide = i
            else:
                usedivide = table[d - 1][i - 1] + rounding(prices[i - 1])
                dontdivide = table[d][last_divide] + rounding(sum(prices[last_divide: i]))
                
                print(table[d][last_divide], sum(prices[last_divide: i]), rounding(sum(prices[last_divide + 1: i])))
                print("divide: ", usedivide, "no divide: ", dontdivide)
                print("last divide: ", last_divide)

                
                if usedivide < dontdivide:
                    print("use divide")
                    last_divide = i - 1
                    print("new last_divide: ", last_divide)

                    total = usedivide
                    table[d][i] = total
                else:
                    print("no divide")
                    print("total: ", total, "no divide: ", dontdivide)
                    total = dontdivide
                    table[d][i] = total
            
            print("d: ", d, "i: ", i)
            pretty_print(table)
            print()
                    
    return table

def cents(items, dividers, prices):
    table = []
    for i in range(dividers + 1):
        line = []
        for j in range(items + 1):
            line.append(sys.maxsize)
        table.append(line)

    #cost = recursive_cents(table, items, dividers, dividers, prices, items)
    cost = non_recursive_cents(table, items, dividers, prices)
    # cost = recursive_cents(table, 0, dividers, prices, 0)
    # print()
    # pretty_print(table)
    # print()
    print (cost[dividers][items])
    
    
def pretty_print(table):
    for i in range(len(table)):
        print(table[i])
        
def main():
    #items, dividers  = map(int, input().split())
    #prices = [int(x) for x in sys.stdin.readline().split()]
    items = 5
    dividers = 4
    prices = [14, 24, 54, 60, 44]
    cents(items, dividers, prices)

if __name__ == "__main__":
    main()