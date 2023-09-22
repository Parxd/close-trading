import pandas as pd

class DataPreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    def preprocessing(self):
        if self.df is None:
            print("Data not loaded. Run load_data() first.")
            return
        
        # Drop 'far_price' and 'near_price' columns
        self.df.drop(['far_price', 'near_price'], axis=1, inplace=True)
        
        # Columns to check for NaN values
        columns_to_check = ['imbalance_size', 'reference_price', 'matched_size', 'bid_price', 'ask_price', 'wap', 'target']
        
        # Drop rows with NaN values in columns_to_check
        self.df.dropna(subset=columns_to_check, inplace=True)
