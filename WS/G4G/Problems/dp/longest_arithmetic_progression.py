"""
Arithmetic progression is set of numbers in which difference between two consecutive numbers is constant.
For example, 1,4,7,10,13 form a arithmetic progression. Given a set of integers in sorted order, find the length of
longest arithmetic progression.
A[i], A[j] and A[k] form an AP if 2* A[j] = A[i] + A[k] where k>j and i<j.

	1	7	10	15	27	29
1	1	2	2	2	2	3
7	0	1	2	2	2	2
10			1	2	2	2
15				1	2	2
27					1	2
29						1

1, 1 represents array of length 1 starting at one and ending at 1
all one length cells are initialized with 1
all two lengths are initialized with 2. since array is sorted
from 3, check formula:
i,j,k is ap if you find (i + k) / 2 in between i and k as j
take 4 at a time, 5 at a time etc and search middle elements for (i + k) /2
"""
#todo