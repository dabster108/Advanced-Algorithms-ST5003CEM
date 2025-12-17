'''Radix Sort is a non-comparative sorting algorithm that sorts numbers digit by digit, 
starting from the least significant digit (LSD) to the most significant digit (MSD), or vice versa. It uses counting sort (or a stable sort) as a subroutine for sorting each digit.
Working Mechanism (LSD approach):
Find the maximum number to know the number of digits.
Start sorting the list from the least significant digit.
Use stable counting sort for each digit.
Move to the next significant digit and repeat until the most significant digit is sorted.'''

'''
We move like from 10's place to 100's place to 1000's place and so on comparing the digits 
'''

list_numbers = [170, 45, 75, 90, 802, 24, 2, 66]

