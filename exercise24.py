#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:29:13 2022

@author: thomas
"""

class Account:
    def __init__(self,name,num,bal):
        self.fname = name
        self.number = num
        self.balance = bal
        
    def deposit(self,am):
        self.balance+= am
        
    def withdraw(self,am):
        if self.balance>= am:
            self.balance-=am
            print('You have withdrawn:',am)
        else:
            print('Insufficient Funds')
    
    def display(self):
        print('Account Number:',self.number)
        print('Account Name:',self.fname)
        print('Account Balance:',self.balance)
        
class MonkeyMarketAccount(Account):
    def __init__(self,name,num,bal):
        
    
        Account.__init__(self,name,num,bal)

x = MonkeyMarketAccount('Me',20,3300)

x.display()
x.withdraw(10000)
x.deposit(2000)
x.display()
