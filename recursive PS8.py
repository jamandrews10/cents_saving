#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:08:32 2024

@author: kaihaesslein
"""
import sys


def get_col(table, col):
    
    col_vals = []
    for row in table:
        col_vals.append(row[col])
   
    return col_vals
    
    
def get_row(m_total, m_used):
    
    row = 0
    
    for i in range(4):
        row <<= m_total[i]
        cur_mask = 0
        for j in range(m_used[i]):
            cur_mask <<= 1
            cur_mask |= 1
        row |= cur_mask
        
    return row

def get_min_coins(data):
    
    first_col = get_col(data, 0)
    second_col = get_col(data, 1)
    
    min_coins = sys.maxsize
    
    for i in range(len(second_col)):
        
        if second_col[i] < min_coins:
            min_coins = second_col[i]
    
    if min_coins != sys.maxsize:
        return min_coins
    
    else:
        
        for i in range(len(first_col)):
            
            if first_col[i] < min_coins:
                min_coins = first_col[i]
    
        return min_coins


def recursive_change(c, coins_used, m_val, m_total, m_used, data):
   # print("c: ", c, "row: ", get_row(m), "v: ", v, "n_used: ", coins_used)
    #print("m: ", m)
   # print()
    
    if c == 0:
        if coins_used <= data[get_row(m_total, m_used)][1]:
            data[get_row(m_total, m_used)][1] = coins_used
            return coins_used
            
    elif c < 0:
        if coins_used <= data[get_row(m_total, m_used)][0]:
            data[get_row(m_total, m_used)][0] = coins_used
            return coins_used
            
    elif data[get_row(m_total, m_used)][c + 1] != sys.maxsize:
        return data[get_row(m_total, m_used)][c + 1]
            
    else:
        
        min_coins = sys.maxsize
        cur_m_used = m_used[:]
        
        for i in range(4):

            if cur_m_used[i] < m_total[i]:
                m_used = cur_m_used[:]
                m_used[i] += 1
                cur_min_coins = recursive_change(c - m_val[i], coins_used + 1, m_val, m_total, m_used, data)
                
                if cur_min_coins < min_coins:
                    min_coins = cur_min_coins
            
                    
        data[get_row(m_total, cur_m_used)][c + 1] = cur_min_coins
        return cur_min_coins
    
        
def check_IOU(c, q, d, n, p):
    return c <= (25 * q) + (10 * d) + (5 * n) + p


def ABC(c, q, d, n, p):
    
    if not(check_IOU(c, q, d, n, p)):
        return "IOU"
    
    else:
        total_coins = q + d + n + p
    
        data = []
        for i in range((2 ** total_coins) + 1):
            cur_row = []
            for j in range(c + 2):
                cur_row.append(sys.maxsize)
            data.append(cur_row)
         
        m_val = [25, 10, 5, 1]
        m_total = [q, d, n, p]
        m_used = [0, 0, 0, 0]
        
        min_coins = recursive_change(c, 0, m_val, m_total, m_used, data)
        
        return get_min_coins(data)


def main():
    
    c = 59
    q = 2
    d = 3
    n = 0
    p = 9
    
    min_coins = ABC(c, q, d, n, p)
    print(min_coins)


main()