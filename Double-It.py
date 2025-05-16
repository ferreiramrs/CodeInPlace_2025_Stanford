""" Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4
8
16
32
64
128 """

import math 

def main():
    """
    You should write your code here. 
    """
    # 1. User input their number:
    user_input = int(input("Enter a number: "))    
    
    # 2. The program will calculate the num * 2 :
    curr_value = user_input*2

    # 3. The program will use the result to make a linear progression:
    while curr_value < 100:
     print(curr_value)
     curr_value = curr_value * 2

    print(curr_value) 
if __name__ == '__main__':
    main()