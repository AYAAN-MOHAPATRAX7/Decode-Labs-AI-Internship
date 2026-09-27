# Project 2: Data Classification Using AI
# DecodeLabs Artificial Intelligence Internship
#
# Algorithm: K-Nearest Neighbors (KNN)
# Dataset: Iris Dataset


# --------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# --------------------------------------------------

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    classification_report
)


# --------------------------------------------------
# 2. LOAD THE IRIS DATASET
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names


print("=" * 60)
print("       DECODELABS - PROJECT 2")
print("       DATA CLASSIFICATION USING AI")
print("=" * 60)

print("\nDataset Information")
print("-" * 60)
print("Number of samples :", X.shape[0])
print("Number of features:", X.shape[1])
print("Number of classes :", len(target_names))

print("\nFeatures:")
for feature in feature_names:
    print("-", feature)

print("\nClasses:")
for target in target_names:
    print("-", target)


# --------------------------------------------------
# 3. SPLIT DATA INTO TRAINING AND TESTING SETS
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nData Split")
print("-" * 60)
print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])


# --------------------------------------------------
# 4. FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --------------------------------------------------
# 5. CREATE KNN CLASSIFICATION MODEL
# --------------------------------------------------

model = KNeighborsClassifier(n_neighbors=5)


# --------------------------------------------------
# 6. TRAIN THE MODEL
# --------------------------------------------------

model.fit(X_train, y_train)


# --------------------------------------------------
# 7. MAKE PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 8. EVALUATE THE MODEL
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

matrix = confusion_matrix(
    y_test,
    y_pred
)


# --------------------------------------------------
# 9. DISPLAY RESULTS
# --------------------------------------------------

print("\nModel Evaluation")
print("-" * 60)

print(f"Accuracy : {accuracy * 100:.2f}%")
print(f"F1 Score : {f1:.2f}")

print("\nConfusion Matrix:")
print(matrix)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=target_names
    )
)


# --------------------------------------------------
# 10. FINAL RESULT
# --------------------------------------------------

print("=" * 60)
print("Model training and evaluation completed successfully.")
print("=" * 60)