import sys

def sel(n):
    s = []
    for i in range(0,len(n)):
        index_to_move = index_of_min(n)
        a = n.pop(index_to_move)
        s.append(a)
    return s



def index_of_min(n):

    min_index = 0
    for i in range(1, len(n)):
        if n[i] < n[min_index]:
            min_index = i
    return min_index



num = [10,6,3,90,4]

print(sel(num))