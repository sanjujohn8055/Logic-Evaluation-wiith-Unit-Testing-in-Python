# src/database.py

import pandas as pd
from sqlalchemy import create_engine

class DatabaseHandler:
    """
    Handles SQLite database operations including creating tables and inserting data.
    """
    def __init__(self, db_path='sqlite:///ideal_function_mapper.db'):
        self.engine = create_engine(db_path)

    def save_dataframe(self, df: pd.DataFrame, table_name: str):
        """
        Saves a pandas DataFrame to the SQLite database.
        
        Parameters:
        - df: DataFrame to save
        - table_name: Name of the target table
        """
        try:
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            print(f"✅ Saved '{table_name}' to database.")
        except Exception as e:
            print(f"❌ Failed to save '{table_name}' to database: {e}")

    def read_table(self, table_name: str) -> pd.DataFrame:
        """
        Reads a table from the database and returns it as a DataFrame.
        
        Parameters:
        - table_name: Table name to read
        """
        try:
            df = pd.read_sql_table(table_name, self.engine)
            return df
        except Exception as e:
            print(f"❌ Failed to read '{table_name}' from database: {e}")
            return pd.DataFrame()
