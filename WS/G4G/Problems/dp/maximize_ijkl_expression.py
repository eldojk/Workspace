# coding=utf-8
"""
http://www.geeksforgeeks.org/maximize-arrj-arri-arrl-arrk-such-that-i-j-k-l/

find the maximum value of arr[l] – arr[k] + arr[j] – arr[i], such that i < j < k < l

table1[] should store the maximum value of arr[l]
table2[] should store the maximum value of arr[l] – arr[k]
table3[] should store the maximum value of arr[l] – arr[k] + arr[j]
table4[] should store the maximum value of arr[l] – arr[k] + arr[j] – arr[i]

Then the maximum value would be present in index 0 of table4 which will be our required answer.
"""

# todo later
