# Import libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# ---------------------------------------------------
# STEP 1: Load Dataset
# ---------------------------------------------------

# Load iris dataset
iris = load_iris()

# Convert dataset into DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column
df['target'] = iris.target

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# ---------------------------------------------------
# STEP 2: Prepare Features and Labels
# ---------------------------------------------------

# Features (input data)
X = iris.data

# Labels (output classes)
y = iris.target

# ---------------------------------------------------
# STEP 3: Split Data into Training and Testing Sets
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))

# ---------------------------------------------------
# STEP 4: Train Classification Model
# ---------------------------------------------------

# Create classifier
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# ---------------------------------------------------
# STEP 5: Make Predictions
# ---------------------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------------------
# STEP 6: Evaluate Model
# ---------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))