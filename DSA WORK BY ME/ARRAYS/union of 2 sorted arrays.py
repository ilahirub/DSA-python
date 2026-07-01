''' QUESTION:-
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.

Example 1:
Input:
n = 5, arr1[] = {1, 2, 3, 4, 5}
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including
both the arrays are: 1 2 3 4 5.

Example 2:
Input:
n = 5, arr1[] = {2, 2, 3, 4, 5}
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including
both the arrays are: 1 2 3 4 5.

APPROACH:-
-> Take two pointer i and j where i is for arr1 and j is for arr2 and traverse
-> While travsersing 3 cases arises
    -> arr1[ i ] == arr2[ j ]
        Here we found a common element, so insert only one element in the union.
        Let’s insert arr[i] in union and whenever we insert element we increment pointer while pointer is not equal to the inserted element
    -> arr1[i]<arr2[j]
        Here insert arr[i]
    -> arr1[i]>arr2[j]
        Here insert arr2[j]
-> Now check if elements of any array is left to traverse then traverse that array

// TIME COMPLEXITY = O(N+M)
// SPACE COMPLEXITY = O(0)   '''
from unittest import result

arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]
i=0
j=0
result = []
while i<len(arr1) and j<len(arr2):
    if arr1[i]==arr2[j]:
        result.append(arr1[i])
        i+=1
        j+=1

    elif arr1[i]<arr2[j]:
        result.append(arr1[i])
        i+=1
    else:
        result.append(arr2[j])
        j+=1

while i<len(arr1):
    result.append(arr1[i])
    i+=1
while j<len(arr2):
    result.append(arr2[j])
    j+=1

print(result)







































