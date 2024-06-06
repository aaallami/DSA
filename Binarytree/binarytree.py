class TreeNode:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None

    def tree_view(self, space='\t', level=0):
        # if node is empty
        if self is None:
            print(space *level+'@')
            return
        #if the node is a leaf
        if self.left is None and self.right is None:
            print(space*level+str(self.key))
            return
        #if the node is a child
        TreeNode.tree_view(self.right, space, level+1)
        print(space*level+str(self.key))
        TreeNode.tree_view(self.left, space, level+1)

    def traver_in_order(self):
        if self is None:
            return []
        return(TreeNode.traver_in_order(self.left)+[self.key]+TreeNode.traver_in_order(self.right))

    def traver_pre_order(self):
        if self is None:
            return []
        return([self.key]+TreeNode.traver_pre_order(self.left)+TreeNode.traver_pre_order(self.right))

    def traver_post_order(self):
        if self is None:
            return []
        return(TreeNode.traver_post_order(self.right)+[self.key]+TreeNode.traver_post_order(self.left))

    def tree_hight(self):
        if self is None:
            return 0
        return 1+ max(TreeNode.tree_hight(self.left), TreeNode.tree_hight(self.right))
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
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
print(f'travers in order= {tree.tree_view()}')
print(f'travers in order= {tree.traver_in_order()}')
print(f'travers per order= {tree.traver_pre_order()}')
print(f'travers post order= {tree.traver_post_order()}')
print(f"tree hight ={tree.tree_hight()}")

