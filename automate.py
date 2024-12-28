# -*- coding: utf-8 -*-
"""Untitled29.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KT8EKahX-Zli08EKmrHnjibYsDXhT8cd
"""

def clean_csv(file_path, output_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        df = df.dropna()
        df = df.drop_duplicates()
        df.to_csv(output_path, index=False)
        print(f"Data cleaned and saved to {output_path}!")
    except Exception as e:
        print(f"An error occurred: {e}")
input_file = input("Enter the path of the CSV file to clean: ").strip()
output_file = input("Enter the path to save the cleaned CSV file: ").strip()
clean_csv(input_file, output_file)