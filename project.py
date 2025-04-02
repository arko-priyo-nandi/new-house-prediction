import pandas as pd

# Load dataset
df = pd.read_csv("house_prices.csv")

# Display first 5 rows
print(df.head())

# Check dataset info
print(df.info())

# Check missing values
print(df.isnull().sum())



# Fill missing values
df.fillna(df.median(), inplace=True)

# Convert categorical columns to numeric using One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)

# Feature Selection
X = df.drop(columns=["SalePrice"])  # Independent variables
y = df["SalePrice"]  # Target variable

from sklearn.model_selection import train_test_split

# Splitting data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
