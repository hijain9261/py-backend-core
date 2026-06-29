import pandas as pd
from typing import Union

class DataExtr:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def fetch_text(self, separator: str = ",", limit: int = 10) -> pd.DataFrame:
        return pd.read_csv(self.file_path, sep=separator, nrows=limit)
    
    def fetch_json(self, limit: int = 10) -> pd.DataFrame:
        df = pd.read_json(self.file_path)
        return df.head(limit)
    
    def fetch_parquet(self, limit: int = 10) -> pd.DataFrame:
        df = pd.read_parquet(self.file_path)
        return df.head(limit)

if __name__ == "__main__":
    file_location = input("Enter the file location: ").strip()
    obj = DataExtr(file_location)
    
    try:
        if file_location.lower().endswith(".csv"):
            result = obj.fetch_text(separator=",")
            
        elif file_location.lower().endswith(".tsv"):
            result = obj.fetch_text(separator="\t")
            
        elif file_location.lower().endswith(".json"):
            result = obj.fetch_json()
            
        elif file_location.lower().endswith(".parquet"):
            result = obj.fetch_parquet()
            
        else:
            print("Unsupported file format.")
        print(result) 
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
