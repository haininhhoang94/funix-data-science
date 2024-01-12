# %%
import numpy as np
import pandas as pd

# %%
# Sample Iris dataset
data = pd.read_csv(
    "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
)
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values  # Labels


# %%
# Define a class for Decision Tree Node
class DecisionNode:
    def __init__(
        self, gini, num_samples, num_samples_per_class, predicted_class
    ) -> None:
        self.gini = gini  # Gini impurity of the node
        self.num_samples = num_samples  # Total number of samples at this node
        self.num_samples_per_class = (
            num_samples_per_class  # Number of samples per class at this node
        )
        self.predicted_class = (
            predicted_class  # Predicted class label for this node
        )
        self.feature_index = 0  # Index of feature to split on
        self.threshold = 0  # Threshold value for the split
        self.left = None  # Left child node
        self.right = None  # Right child node


# Define a class for te Decision Tree Classifier
class DecisionTreeClassifier:
    def fit(self, X, y):
        self.n_classes = len(np.unique(y))  # Number of classes
        self.n_features = X.shape[1]  # Number of features
        self.tree = self._build_tree(X, y)

    def _build_tree(self, X, y, depth=0):
        num_samples_per_class = [np.sum(y == i) for i in range(self.n_classes)]
        predicted_class = np.argmax(num_samples_per_class)
        node = DecisionNode(
            gini=self._gini(y),
            num_samples=len(y),
            num_samples_per_class=num_samples_per_class,
            predicted_class=predicted_class,
        )

        # Check termination conditions
        if depth < 2:
            if len(np.unique(y)) == 1:
                return node
            if X.shape[0] <= 2:
                return node

        # Find the best split
        feature_index, threshold = self._find_best_split(X, y)
        if feature_index is not None:
            indices_left = X[:, feature_index] < threshold
            X_left, y_left = X[indices_left], y[~indices_left]
            X_right, y_right = X[~indices_left], y[~indices_left]
            node.feature_index = feature_index
            node.threshold = threshold
            node.left = self._build_tree(X_left, y_left, depth + 1)
