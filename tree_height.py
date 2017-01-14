def getHeight(self,root):
    if root is None:
        return 0
    else:
        print(root.data)
        lh = getHeight(root.left)
        rh = getHeight(root.right)
        print(root.data)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1
