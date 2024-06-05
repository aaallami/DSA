class TreeNode:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

def tree_view(node, space, level):
    # if node is empty
    if node is None:
        print(space *level+'@')
        return
    #if the node is a leaf
    if node.left is None and node.right is None:
        print(space*level+str(node.key))
        return
    #if the node is a child
    tree_view(node.right, space, level+1)
    print(space*level+str(node.key))
    tree_view(node.left, space, level+1)

def traver_in_order(node):
    if node is None:
        return []
    return(traver_in_order(node.left)+[node.key]+traver_in_order(node.right))

def traver_pre_order(node):
    if node is None:
        return []
    return([node.key]+traver_pre_order(node.left)+traver_pre_order(node.right))

def traver_post_order(node):
    if node is None:
        return []
    return(traver_post_order(node.right)+[node.key]+traver_post_order(node.left))

def tree_hight(node):
    if node is None:
        return 0
    return 1+ max(tree_hight(node.left), tree_hight(node.right))
        
    
node0=TreeNode(3)
node1=TreeNode(4)
node2=TreeNode(5)
node3=TreeNode(6)
#node4=TreeNode(None)
#node5=TreeNode(None)
node6=TreeNode(7)

node0.left=node1
node0.right=node2
node1.left=node3
#node1.right=node4
#node2.left=node5
node2.right=node6
tree =node0
print(f"tree, {tree.key}")
print(f'travers in order= {traver_in_order(tree)}')
print(f'travers per order= {traver_pre_order(tree)}')
print(f'travers post order= {traver_post_order(tree)}')
print(f"tree hight ={tree_hight(tree)}")
tree_view(tree, '     ', 0)
