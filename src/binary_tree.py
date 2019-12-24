import string

class TreeNode:
    def __init__(self, key, val, parent=None, left=None, right=None):
        self.left=left
        self.right=right
        self.parent=parent
        self._key=key
        self._val=val

    @property
    def key(self):
        return self._key

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, v):
        if v not in string.ascii_letters:
            raise ValueError('{} is wrong value'.format(v))
        self._val=v

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)


    def __repr__(self):
        return f'TreeNode(key={self.key}, val={self.val})'

class BinaryTree:

    def __init__(self, tree_dict):
        sorted_keys=sorted(tree_dict.keys())
        self.root=BinaryTree.build(sorted_keys, tree_dict, 0, len(tree_dict) - 1)
        self.size=len(tree_dict)

    def _most_left(self, node):
        while node and node.left:
            node=node.left
        return node

    def __iter__(self):
        self.cur=self._most_left(self.root)
        return self

    def _is_right_child(self, node):
        return False if (not node or not node.parent) else id(node.parent.right) == id(node)

    def __next__(self):
        if not self.cur:
            raise StopIteration()
        val=self.cur.val

        if self.cur.right:
            self.cur = self._most_left(self.cur.right)
        elif not self.cur.parent:
            self.cur = None
        else:
            node=self.cur
            while self._is_right_child(node):
                node=node.parent
            self.cur=node.parent

        return val

    def _walk(self, node):
        if not node:
            return

        yield from self._walk(node.left)
        yield node.val
        yield from self._walk(node.right)

    def values(self):
        yield from self._walk(self.root)

    def find(self, key):
        cur = self.root
        while True:
            if not cur:
                return None
            if cur.key == key:
                return cur.val
            cur = cur.left if cur.key > key else cur.right

    @staticmethod
    def build(sorted_keys, tree_dict, start, end):
        if start > end:
            return None

        mid=(start + end) // 2
        key=sorted_keys[mid]
        node = TreeNode(key=key, val=tree_dict[key])
        node.left = BinaryTree.build(sorted_keys, tree_dict, start, mid - 1)
        if node.left:
            node.left.parent = node
        node.right = BinaryTree.build(sorted_keys, tree_dict, mid + 1, end)
        if node.right:
            node.right.parent = node
        return node

    def find_root2leaf_with_sum(self, trace=[], result=[], pred=lambda x:True):
        '''
            Discover the list from root to leaf that sum of all elements alone the path meet the predicate
        '''
        return self.find_root2leaf(self.root, pred, trace, result)
        
    def find_root2leaf(self, cur, pred, trace, result):
        if not cur:
            return
        if cur.is_leaf():
            trace.append(cur.key)
            if pred(sum(trace)):
                result.append(trace.copy())
            trace.pop()
            return

        trace.append(cur.key)
        self.find_root2leaf(cur.left, pred, trace, result)
        self.find_root2leaf(cur.right, pred, trace, result)
        trace.pop()
