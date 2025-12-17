'''Insertion Sort is a sorting algorithm that builds a sorted part of the 
list one element at a time. It takes each element from 
the unsorted part and inserts it into its correct position in the sorted part.
'''
'''
Base case : O(n)
Average case : O(n^2)
Worst case : O(n^2)
'''
# Insertion Sort in Python

numbers = [4, 5, 6, 7]
for i in range(1, len(numbers)):
    temp = numbers[i]  
    j = i - 1
    while j >= 0 and numbers[j] > temp:
        numbers[j + 1] = numbers[j]
        j = j -1 
    numbers[j + 1] = temp  

print("Sorted list:", numbers)









'''
Suppose j = 0 and numbers[0] > temp.

We move numbers[0] one position to the right: numbers[1] = numbers[0].

Then we do j = j - 1, so j becomes -1.

Now the while condition is checked: j >= 0 and numbers[j] > temp.

j >= 0 is false because j = -1.

The loop stops immediately, so Python does not try to access numbers[-1] in this iteration.

After the loop, we insert temp at numbers[j + 1].

j + 1 = -1 + 1 = 0 → we insert temp at index 0.'''