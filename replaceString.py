# replace a string in an array
def replaceG(l):
    res = [sub.replace('g','_').replace('_','e') for sub in l]
    return res
# return duplicates in an array
def duplicate(arr):
    d =[]
    for i in arr:
        n = arr.count(i)
        if n > 1 and i not in d:
            d.append(i)
    return d
def duplicate(arr):
    d =set()
    for i in range(len(arr)) :
       for j in range(i+1, len(arr)):
           if arr[i] == arr[j]:
               d.add(arr[i])
               
    return d
if __name__ == "__main__":
    print(duplicate([4,4,3,5,6]))