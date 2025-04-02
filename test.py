import pickle

with open("columns.pkl", "rb") as f:
    data_columns = pickle.load(f)

print("Total columns:", len(data_columns))
print("First 10 columns:", data_columns[:10])
print("Location columns:", data_columns[3:])  # Locations should start from index 3
