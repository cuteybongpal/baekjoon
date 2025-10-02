a = int(input())
tree = {}
key = ''
for i in range(a):
    root, child1, child2 = input().split()
    tree[root] = (child1, child2)
    if key == '':
        key = root
    

pre_list = []
#전위 순회
def preorder(a:dict, key:str) ->list:
    if key not in a or key == '.':
        return
    pre_list.append(key)
    preorder(a, a[key][0])
    preorder(a, a[key][1])
in_list = []
#중위 순회
def inorder(a:dict, key:str)->list:
    if key not in a or key == '.':
        return
    inorder(a, a[key][0])
    in_list.append(key)
    inorder(a, a[key][1])

post_list = []
#후위 순회
def postorder(a:dict, key:str)->list:
    if key not in a or key == '.':
        return
    postorder(a, a[key][0])
    postorder(a, a[key][1])
    post_list.append(key)
preorder(tree, key)
inorder(tree, key)
postorder(tree, key)
print("".join(pre_list))
print("".join(in_list))
print("".join(post_list))
