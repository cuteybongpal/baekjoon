import sys
sys.setrecursionlimit(10**6)
binary_tree = {}
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

def add_data_into_binary_tree(a:dict, b:int):
    idx = 0
    key = nums[0]
    while True:
        if key not in a:
            a[key] = [0, 0]
            break
        if key > b:
            if a[key][0] == 0:
                a[key][0] = b
                a[b] = [0,0]
                break
            else:
                key = a[key][0]
        else:
            if a[key][1] == 0:
                a[key][1] = b
                a[b] = [0,0]
                break
            else:
                key = a[key][1]

for i in nums:
    add_data_into_binary_tree(binary_tree, i)


post_list = []
#후위 순회
def postorder(a:dict, key:int)->list:
    if key not in a or key == 0:
        return
    postorder(a, a[key][0])
    postorder(a, a[key][1])
    post_list.append(key)
    
postorder(binary_tree, nums[0])
print("\n".join(map(str, post_list)))
