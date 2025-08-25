# EDA-in-python

A lightweight Python EDA pipeline for a Udemy Finance & Accounting courses dataset that performs basic cleaning, numeric coercion, exploratory visualizations, a correlation heatmap, and saves a cleaned CSV for downstream analysis.

Features
Loads a CSV dataset of Udemy Finance/Accounting courses and prints shape and columns for quick verification during runs.

Cleans missing values by filling with the string “Unknown” and coerces key numeric fields to numbers with safe fallback to 0 for non-parsable entries.

Generates distribution plots for rating, price, number of reviews, and number of subscribers when those columns exist, plus a correlation heatmap for all numeric columns.

Requirements
Python with pandas, numpy, seaborn, matplotlib, and warnings/os (standard library) available in the environment.

A CSV file accessible at the configured path (defaults in the script to a local Windows path) or modify the script to point to the dataset location before running.

Data Expectations
Expected numeric columns (if present): rating, num_reviews, num_subscribers, num_lectures, price; these are coerced to numeric with non-numeric values set to 0 after coercion.

Other columns are left as-is, with missing values filled as “Unknown” to avoid null-related plotting or export issues.

Visualizations
Rating distribution histogram with KDE if rating column exists.

Price distribution histogram with KDE if price column exists.

Number of reviews distribution histogram with KDE if num_reviews exists.

Number of subscribers distribution histogram with KDE if num_subscribers exists.

Correlation heatmap across all numeric columns for quick pattern discovery when any numeric data is available.

Output
Saves a cleaned dataset to cleaned_finance_dataset.csv in the working directory after processing.

Prints the current working directory and informative status messages throughout execution for traceability.

Usage
Update the CSV path in the script (pd.read_csv(...)) to point to the local dataset if needed before running.

Run the script in a Python environment with the listed packages installed; visualizations render to screen via matplotlib and seaborn.

Error Handling
Gracefully handles missing file errors with a clear message to check path and file existence.

Catches generic exceptions with guidance to verify CSV formatting, required columns, and data types if issues arise during load or processing.

Notes and Extensibility
The script is intentionally minimal and modular; add feature engineering, richer summaries, or additional plots by extending the cleaned dataframe section.

For reproducibility in different environments, consider parameterizing the CSV path and adding a requirements.txt with pinned versions for pandas, numpy, seaborn, and matplotlib.

Repository Structure (suggested)
EDA-in-python.py — main analysis script for loading, cleaning, plotting, and exporting the cleaned dataset.
EDA in python ouutput.pdf -  final outputs and graphs 
