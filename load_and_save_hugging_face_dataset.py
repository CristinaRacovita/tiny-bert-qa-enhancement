import pandas as pd
from datasets import load_dataset

# Load the Hugging Face dataset (replace 'dataset_name' with the name of your dataset)
dataset = load_dataset("squad")

# Convert the dataset to a Pandas DataFrame
validation = pd.DataFrame(dataset["validation"])
train = pd.DataFrame(dataset["train"])
# Specify the path to save the CSV file
VALIDATION_CSV_FILE_PATH = "data/squad_validation.csv"
TRAIN_CSV_FILE_PATH = "data/squad_train.csv"

# Save the DataFrame to a CSV file
validation.to_csv(VALIDATION_CSV_FILE_PATH, index=False)
train.to_csv(TRAIN_CSV_FILE_PATH, index=False)
