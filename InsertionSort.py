
import Tools


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while (i > -1) and (a[i] > key):
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


# create random array with at most 50 unrepeated elements within range 0 to 99
a = []
Tools.fill_random_array(a)
print(a)
insertion_sort(a)
print(a)















