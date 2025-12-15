
def bookends(li: list):
    """
    Given a list of numbers remove the first and last elements from the list and
    return a new list of those two elements.
    You can assume any list given is at least 2 elements long.
    Example list of [1,5,7,3,2] the original list would become [5,7,3] and the new
    list would be [1,2]
    :param list:
    :return:
    """
    firstNumber = li[0]
    lastNumber = li[len(li)-1]
    print(lastNumber)
    li.pop(0)
    li.pop(-1)
    print(li)
    newList = [firstNumber, lastNumber]
    print(newList)
    return newList

def inOrder(li : list):
    """
    Given a list of numbers return true if the list is in ascending order.
    :param list:
    :return:
    """
    n = len(li)
    x = 0
    answer = True
    while x<n-1 and answer == True:
        if li[x]<li[x+1]:
            answer = True
            x+=1
        else:
            answer = False
    print(answer)
    return(answer)






def find(li: list, target : int):
    """
    Given a list of numbers and a target value return the index location of the
    target value within the list.
    If the target value is not in the list return -1
    If multiple of the target value exist within the list you may return either
    index.
    You are not allowed to use the built-in index method from python.
    Example list [1,3,5,7,9] target = 3 returned value would be 1 because 3 can be
    found at the first index.
    Example list [3, 7, 8, 1, 0, 1, 12] target = 1 a return of either 3 or 5 would
    be valid.
    Example list [1,3,5,6,9] target 7 returns -1 because 7 is not within the list.
    :param list:
    :param target:
    :return:
    """
    n = 0
    x = 0
    lastIndex = len(li)-1
    while li[n] != target:
        if n<=lastIndex-1:
            n+=1
            x+=1
        else:
            x = -1
            break
    print(x)
    return(x)

def removeLowest(li):
    """
    Given a list of numbers remove the lowest element from the list. You may assume the list is at least 1 element long.
    If there are multiple of the lowest number you just need to remove 1.
    Example list [3,6,7,2,12] would become [3,6,7,12]
    :param list:
    :return:
    """
    n = 0
    x = 1
    answerIndex = 0
    lastIndex = len(li)-1
    while x <= lastIndex:
        if li[n] > li[x]:
            n=x
            x+=1
            answerIndex = n
        else:
            x+=1
    li.pop(answerIndex)


def keepOrder(li: list, value):
    """
    Given a list of numbers that is in order and a value. Place the value into the
    list such that the list is still in order.
    Example list=[1,3,5,6] value =4 the resulting list would be [1,3,4,5,6]
    :param list:
    :param value:
    :return:
    """
    x = 0
    length = len(li)
    while value > li[x]:
        if x < length-1:
            x += 1
        else:
            x = len(li)
            break
    li.insert(x,value)
    print(li)
    return(li)



def merge(l1:list, l2:list):
    """
    Given two lists that are in order. produce a new list that is the two lists merged together and in order.
    Make sure to now modify either of the original lists.
    Example l1 = [1,3,5] l2 = [2,4,6,8] -> [1,2,3,4,5,6,8]
    :param l1:
    :param l2:
    :return:
    """
    n1 = 0
    n2 = 0
    length1 = len(l1)
    length2 = len(l2)
    totalLength = length1 + length2
    newList = []
    while n1+n2 < totalLength-2:
        if l1[n1] < l2[n2]:
            newList.append(l1[n1])
            n1 += 1
        else:
            newList.append(l2[n2])
            n2 += 1
    if n1-1<n2-1:
        newList.append(l1[length1-2])
    else:
        newList.append(l2[length2 - 2])
    if n1<n2:
        newList.append(l1[length1 - 1])
    else:
        newList.append(l2[length2 - 1])
    print(newList)
    return(newList)

    