# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import seaborn as sns

# %%
cell_df = pd.read_csv("./cell_samples.csv")
# %%
# Check the Class to see how many class in cell samples exist
sns.histplot(cell_df["Class"], discrete=True)
print(cell_df["Class"].unique())
# So the class only either have Benign Tumor (ung thu lanh tinh - 2) hoac Malignant tumor (ung thu ac tinh - 4)
# %%
# Let's investigate Clump with Unifsize
# Scatter plot
plt.title(label="Scatter plot Clump vs Unifsize")
sns.scatterplot(
    data=cell_df,
    x="Clump",
    y="UnifSize",
    hue="Class",
    palette=["yellow", "red"],
)
plt.show()
# %%
# Check dtypes by data wrangler or
# cell_df.dtypes
# So the BareNuc contain a ? inside it. Let's drop it
# First convert into numeric
cell_df = cell_df[pd.to_numeric(cell_df["BareNuc"], errors="coerce").notnull()]
# convert all col to int
for col_ in cell_df.columns:
    cell_df[col_] = cell_df[col_].astype("int")

# %%
# Let's set target and features
X = np.asanyarray(cell_df.drop(columns=["ID", "Class"]))
y = np.asanyarray(cell_df["Class"])

# %%
# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# %%
# Using SVM with Radial Basis Function
from sklearn import svm

clf = svm.SVC(kernel="rbf")
clf.fit(X=X_train, y=y_train)

# %%
y_pred = clf.predict(X=X_test)

# %%
# Metrics
from sklearn.metrics import classification_report, confusion_matrix

cnf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
labels = ["Positive", "Negative"]
cnf_matrix = pd.DataFrame(cnf_matrix, columns=labels, index=labels)
sns.heatmap(data=cnf_matrix, annot=True)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()

# F1 score
from sklearn.metrics import f1_score

f1_scr = f1_score(y_true=y_test, y_pred=y_pred, average="weighted")
print("F1-score: {:.3f}".format(f1_scr))

# Jaccard score
from sklearn.metrics import jaccard_score

jaccard_scr = jaccard_score(y_true=y_test, y_pred=y_pred, pos_label=2)
print("Jaccard Score: {:.3f}".format(jaccard_scr))

# %%
# Change to use linear
clf = svm.SVC(kernel="linear")
clf.fit(X=X_train, y=y_train)

y_pred = clf.predict(X=X_test)

# Metrics
cnf_matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
labels = ["Positive", "Negative"]
cnf_matrix = pd.DataFrame(cnf_matrix, columns=labels, index=labels)
sns.heatmap(data=cnf_matrix, annot=True)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()

# F1 score
from sklearn.metrics import f1_score

f1_scr = f1_score(y_true=y_test, y_pred=y_pred, average="weighted")
print("F1-score: {:.3f}".format(f1_scr))

# Jaccard score
from sklearn.metrics import jaccard_score

jaccard_scr = jaccard_score(y_true=y_test, y_pred=y_pred, pos_label=2)
print("Jaccard Score: {:.3f}".format(jaccard_scr))

# %%
