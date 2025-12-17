'''
Bucket Sort is a distribution sort that divides the elements into several “buckets” and then sorts each bucket individually. After sorting, the buckets are combined to get the final sorted list. It works well when the input is uniformly distributed.

Working Mechanism:

Create empty buckets (lists). The number of buckets can depend on the input size or range.

Distribute elements into these buckets based on a rule (like dividing by range or maximum value).

Sort each bucket individually (using another sorting algorithm like Insertion Sort).

Concatenate all buckets to get the final sorted list.
'''