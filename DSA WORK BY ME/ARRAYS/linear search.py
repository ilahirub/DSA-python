def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [3,7,2,9,5]
target = 9

result = linear_search(arr, target)

if result != -1:
    print('value', target, 'found at indec', result)
else:
    print('value', target, 'not found')