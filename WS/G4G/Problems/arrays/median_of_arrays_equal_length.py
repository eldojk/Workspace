"""
amzn

http://www.geeksforgeeks.org/median-of-two-sorted-arrays/

1) Calculate the medians m1 and m2 of the input arrays ar1[]
   and ar2[] respectively.
2) If m1 and m2 both are equal then we are done.
     return m1 (or m2)
3) If m1 is greater than m2, then median is present in one
   of the below two subarrays.
    a)  From first element of ar1 to m1 (ar1[0...|_n/2_|])
    b)  From m2 to last element of ar2  (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one
   of the below two subarrays.
   a)  From m1 to last element of ar1  (ar1[|_n/2_|...n-1])
   b)  From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays
   becomes 2.
6) If size of the two arrays is 2 then use below formula to get
  the median.
    Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
"""


def get_median(array1, array2, l1, h1, l2, h2):
    if h1 - l1 == 1 or h2 - l2 == 1:
        print l1, h1, l2, h2
        return (max(array1[l1], array2[l2]) + min(array1[h1], array2[h2])) / 2.0

    if h1 == l1 or h2 == l2:
        return (array1[l1] + array2[l2]) / 2.0

    mid1 = (l1 + h1) // 2
    mid2 = (l2 + h2) // 2

    if array1[mid1] == array2[mid2]:
        return array1[mid1]

    if array1[mid1] < array2[mid2]:
        return get_median(array1, array2, mid1 + 1, h1, l2, mid2 - 1)

    return get_median(array1, array2, l1, mid1 - 1, mid2 + 1, h2)


if __name__ == '__main__':
    print get_median([1, 2, 3, 6, 7], [4, 5, 8, 9, 10], 0, 4, 0, 4)


"""
read up
http://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
"""