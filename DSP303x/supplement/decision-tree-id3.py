# Source: from machinelearningcoban
from __future__ import print_function
import numpy as np
import pandas as np


class TreeNode(object):
    def __init__(self, ids=None, children=[], entropy=0, depth=0) -> None:
        self.ids = ids  # index of data in this node
        self.entropy = entropy  # entropy
        self.depth = depth  # distance to root node
        self.split_attribute = (
            None  # which attributre is chosen, it is a nonleaf node
        )
        self.children = children  # lists of its child nodes
        self.order = None  # order of values of split_attribute in children
        self.label = None  # label of node if it is a leaf

    def set_properties(self, split_attribute, order):
        self.split_attribute = split_attribute  # split at which attribute
        self.order = order  # order of this node's children

    def set_label(self, label):
