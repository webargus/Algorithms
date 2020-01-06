
import Tools


def merge(a, p, q, r):
    n1 = q - p
    n2 = r - q
    left = a[0:n1]
    right = a[n2:]
    i = j = k = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    # copy eventual remaining elements of lists to A
    for ix in range(i, len(left)):
        a[k] = left[ix]
        k += 1
    for ix in range(j, len(right)):
        a[k] = right[ix]
        k += 1


def merge_sort(a):
    if len(a) == 1:
        return
    mid = len(a) // 2
    rest = len(a) % 2
    merge_sort(a[:mid])
    merge_sort(a[mid:])
    merge(a, 0, mid, len(a) - rest)


a = []
Tools.fill_random_array(a)
print(a)
merge_sort(a)

print(a)



















