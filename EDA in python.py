# Step 1: Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import os

warnings.filterwarnings('ignore')

try:
    # Step 2: Load the dataset
    print("Loading dataset...")
    df = pd.read_csv(r"c:\Users\siddh\OneDrive\Desktop\PYTHON\udemy_output_All_Finance__Accounting_p1_p626.csv")
    print(f"Dataset loaded successfully. Shape: {df.shape}")
    print("\nColumns in the dataset:")
    print(df.columns.tolist())
    
    # Step 3: Basic Cleaning
    print("\nCleaning data...")
    # Fill missing values
    df = df.fillna('Unknown')
    
    # Convert numeric columns
    numeric_columns = ['rating', 'num_reviews', 'num_subscribers', 'num_lectures', 'price']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Step 4: Create visualizations based on available columns
    print("\nCreating visualizations...")
    
    # 1. Rating Distribution (if rating column exists)
    if 'rating' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['rating'], bins=20, kde=True)
        plt.title("Distribution of Course Ratings")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    
    # 2. Price Distribution (if price column exists)
    if 'price' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['price'], bins=20, kde=True)
        plt.title("Distribution of Course Prices")
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    
    # 3. Number of Reviews Distribution (if num_reviews column exists)
    if 'num_reviews' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['num_reviews'], bins=20, kde=True)
        plt.title("Distribution of Number of Reviews")
        plt.xlabel("Number of Reviews")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    
    # 4. Number of Subscribers Distribution (if num_subscribers column exists)
    if 'num_subscribers' in df.columns:
        plt.figure(figsize=(10,6))
        sns.histplot(df['num_subscribers'], bins=20, kde=True)
        plt.title("Distribution of Number of Subscribers")
        plt.xlabel("Number of Subscribers")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()
    
    # 5. Correlation Matrix (for all numeric columns)
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        plt.figure(figsize=(10,8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Matrix")
        plt.tight_layout()
        plt.show()
    
    # Step 5: Save cleaned dataset
    print("\nSaving cleaned dataset...")
    df.to_csv("cleaned_finance_dataset.csv", index=False)
    print("Analysis complete! Cleaned dataset saved as 'cleaned_finance_dataset.csv'")

    print("Current working directory:", os.getcwd())

except FileNotFoundError:
    print("Error: udemy_output_All_Finance__Accounting_p1_p626.csv file not found. Please make sure the file exists in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    print("\nPlease check if:")
    print("1. The CSV file is properly formatted")
    print("2. All required columns are present")
    print("3. The data types are correct")

