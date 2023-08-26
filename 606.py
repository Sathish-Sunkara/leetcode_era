def a606(root,st):
    left = "({})".format(a606(root.left)) if root.left or root.right else ""
    right = "({})".format(a606(root.right)) if root.right else ""
    return "{}{}{}".format(root.val,left,right)

    
    



st = ""
class tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
root = tree(10)
root.left = tree(5)
root.right = tree(20)
root.left.left = tree(3)
root.right.right = tree(30)

res = a606(root,st)
print(res)
        
        
    
        
