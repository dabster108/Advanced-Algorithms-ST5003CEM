
'''

Bubble Sort is a simple sorting algorithm that repeatedly compares and swaps adjacent elements 
if they are in the wrong order, moving larger elements to the end step by step . 
It starts from the first element (index 0).

It compares the first element with the next one (index 1).

If the first element is greater, it swaps them.

Then it moves to the next pair (index 1 and index 2) and repeats the same comparison.

This process continues until it reaches the end of the list where the largest element moves to the end like a bubble.

It then starts again from the beginning but this time it goes one step less because the last element is already sorted.


 Best Case (already sorted list):

Only one pass is needed because no swaps happen.

Time Complexity: O(n)

2. Worst Case (reverse order):

Every element has to be compared and swapped many times.

Time Complexity: O(n²)

3. Average Case:

For a random list, it also takes roughly the same number of comparisons and swaps.

Time Complexity: O(n²)
'''
numbers = [5, 2, 4, 1, 3]
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
