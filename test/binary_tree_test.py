from nose import *
from nose.tools import *
from binary_tree import TreeNode
from binary_tree import BinaryTree
from collections import deque

class Test_TreeNode:
    def setup(self):
        self.t = TreeNode(key=1, val='a')

    @raises(ValueError)
    def test_value_set(self):
        self.t.val='?'

    def test_treenode(self):
        assert self.t.key == 1 and self.t.val == 'a'

    def test_treenode_root(self):
        assert self.t.is_root()

    def test_treenode_leaf(self):
        assert self.t.is_leaf()

    def test_repr(self):
        assert str(self.t) == f'TreeNode(key={self.t.key}, val={self.t.val})'

    def test_setter(self):
        self.t.val = 'b'
        assert self.t.val == 'b'

class Test_BinaryTree:
    def setup(self):
        self.test_target='pythonwithlongstringforbinarysearchtree'
        tree_dict=dict(zip(range(len(self.test_target)), self.test_target))
        self.bt=BinaryTree(tree_dict)

    def test_tree_walk(self):
        result=''.join(map(str, self.bt.values()))
        assert self.test_target == result

    def test_tree_find(self):
        assert self.bt.find(len(self.test_target)) == None
        assert self.bt.find(0) == self.test_target[0]
        assert self.bt.find(len(self.test_target) - 1) == self.test_target[-1]

    def test_tree_iterable(self):
        it=iter(self.bt)
        for i in range(len(self.test_target)):
            assert self.test_target[i] == next(it)

    def test_with_deque(self):
        it=iter(self.bt)
        q=deque(it, 2)
        assert ''.join(self.test_target[-2:]) == ''.join(q)

    def test_find_leaf_with_sum(self):
        result=[]
        trace=[]
        func=lambda x: x % 3 == 0
        self.bt.find_root2leaf_with_sum(trace, result, pred=func)
        for i in result:
            assert func(sum(i))

