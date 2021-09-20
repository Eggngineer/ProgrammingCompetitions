sampleList = [1,14, 32, 51, 51, 51, 243, 419, 750, 910]

def binary_search(key) -> int:
    key = int(key)
    left,right = 0, int(len(sampleList))-1

    while(right >= left):
        mid = int(left + (right - left) / 2)
        if sampleList[mid] == key:
            return mid
        elif sampleList[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return -1


#change this in accordance with the problem
#========================================
lst = sampleList
#----------------------------------------
def isOK(lst,index, key) -> bool:
    if lst[index] >= key:
        return True
    else:
        return False
#========================================


def binary_search_generalized(key) -> int:
    left, right = -1, int(len(lst))

    while(right - left > 1):
        mid = int(left + (right - left) / 2)

        if (isOK(lst,mid, key)):
            right = mid
        else:
            left = mid

    return right

if  __name__ == '__main__':
    print(binary_search_generalized(51))
