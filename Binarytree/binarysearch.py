from jovian.pythondsa import evaluate_test_case
tests=[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7}]
test={'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3}

def locate_card(lst, num):
    """
    This solution is O(n), linear search
    """
    pos=0
    if len(lst)==0:
        return -1
    while True:
        if lst[pos]==num:
            return pos
        pos+=1
        if pos==len(lst):
            return -1

def locate_card2(lst, num):
    """
    This solution is O(log(n))
    """
    l, h=0, len(lst)-1
    if len(lst)==0:
        return -1
    #find the middle of the list
    while l<=h:
        mid=(h+l)//2
        mid_num=lst[mid]
        if mid_num==num:
            return mid
        elif mid_num<num:
            h=mid+1
        elif mid_num<num:   
            l=mid-1
    return -1
#linear search 
'''
for test in tests:
    result=locate_card(test['input']['cards'], test['input']['query'])
    if result==test['output']:
        print('pass')
    else:
        print('No pass')
'''
for test in tests:
    result=locate_card2(test['input']['cards'], test['input']['query'])
    if result==test['output']:
        print('pass')
    else:
        print('No pass')
