import pandas as pd
import re

# Function to extract and standardize the entry number
def standardize_entry_number(text):
    text = str(text)  # Convert to string in case it's not
    # Extract the entry number using regex
    match = re.search(r'\d{4}[A-Z]{3}\d{4}', text, re.IGNORECASE)
    if match:
        # Ensure the entry number is in uppercase
        return match.group(0).upper()
    return text  # Return original text if no match (fallback)

# Load the CSV file
df = pd.read_csv('impression_network.csv')

# Remove the 'Timestamps' column
df.drop('Timestamp', axis=1, inplace=True)

# Apply the transformation to the 'Email Address' column
df['Email Address'] = df['Email Address'].apply(standardize_entry_number)

# Apply the transformation to each 'Your Impression #' column
for column in df.columns:
    if column.startswith('Your Impression'):
        df[column] = df[column].apply(standardize_entry_number)

# Optionally, save the modified DataFrame to a new CSV file
df.to_csv('modified_impression_network.csv', index=False)

