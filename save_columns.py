import pickle

# Replace these with actual location names from your dataset
columns = ['total_sqft', 'bath', 'bhk', 'Indira Nagar', 'Whitefield', 'Electronic City', 'other']

# Save columns to a pickle file
pickle.dump(columns, open("columns.pkl", "wb"))

print("✅ columns.pkl created successfully!")
