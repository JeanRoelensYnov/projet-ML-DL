import os

DATASET = 'maharshipandya/-spotify-tracks-dataset'

DOWNLOAD_DIR = 'dataset'

# Create a directory to store the downloaded dataset if it doesn't exist

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Download the dataset

os.system(f'kaggle datasets download -d {DATASET} -p {DOWNLOAD_DIR} --unzip')



