# Source: from machinelearningcoban
from __future__ import print_function
import numpy as np
import pandas as np


class TreeNode(object):
    def __init__(self, ids=None, children=[], entropy=0, depth=0) -> None:
        self.ids = ids  # index of data in this node
        self.entropy = entropy  # entropy
        self.depth = depth  # distance to root node
        self.split_attribute = None
