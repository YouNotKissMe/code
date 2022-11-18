class binary_trees: 
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.right = right
        self.left = left
    def __str__(self):
        return self.item

def right_lists(main_list,arr=[]):
    if main_list.right == None:
        return print(arr+[main_list.item])
    else:
        arr.append(main_list.item)
        right_lists(main_list.right,arr)

def func(trees, item,arr):
    if item > trees.item and trees.right == None:
        trees.right = binary_trees(item)
        arr.append(binary_trees(item))

    elif item > trees.item and trees.right:
        func(trees.right, item,arr)
    if item < trees.item and trees.left == None:
        trees.left = binary_trees(item)
        arr.append(binary_trees(item))

    elif item < trees.item and trees.left:
        func(trees.left, item,arr)


test = [2, 4, 6, 8, 7, 3,12,45,3,9,55]
arr_trees = []
for i in test:
    if arr_trees == []:
        arr_trees.append(binary_trees(i))
    else:
        func(arr_trees[0], i,arr_trees)

right_lists(arr_trees[0])