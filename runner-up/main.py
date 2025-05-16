if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


list2 = [ x for x in arr if x < max(arr) ]

runnerUp = set([ y for y in list2 if y == max(list2)])

print (str(next(iter(runnerUp))))
