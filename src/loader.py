# # import pandas as pd
# # import os

# # BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # this goes up from /src to project root

# # def load_train_data():
# #     return pd.read_csv(os.path.join(BASE_DIR, "data", "train1.csv"))

# # def load_ideal_data():
# #     return pd.read_csv(os.path.join(BASE_DIR, "data", "ideal.csv"))

# # def load_test_data():
# #     return pd.read_csv(os.path.join(BASE_DIR, "data", "test.csv"))

# import pandas as pd
# import os

# # This goes up from /src to project root
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# def load_train_data() -> pd.DataFrame:
#     """Loads the training dataset with 4 y functions"""
#     return pd.read_csv(os.path.join(BASE_DIR, "data", "train1.csv"))

# def load_ideal_data() -> pd.DataFrame:
#     """Loads the 50 ideal functions dataset"""
#     return pd.read_csv(os.path.join(BASE_DIR, "data", "ideal.csv"))

# def load_test_data() -> pd.DataFrame:
#     """Loads the test dataset with x-y pairs"""
#     return pd.read_csv(os.path.join(BASE_DIR, "data", "test.csv"))

# def get_data_paths():
#     """Returns dictionary of absolute file paths used throughout the project"""
#     return {
#         "train": os.path.join(BASE_DIR, "data", "train1.csv"),
#         "ideal": os.path.join(BASE_DIR, "data", "ideal.csv"),
#         "test": os.path.join(BASE_DIR, "data", "test.csv"),
#     }

import pandas as pd
import os

# This goes up from /src to project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_train_data() -> pd.DataFrame:
    """Loads the training dataset with 4 y functions"""
    return pd.read_csv(os.path.join(BASE_DIR, "data", "train1.csv"))

def load_ideal_data() -> pd.DataFrame:
    """Loads the 50 ideal functions dataset"""
    return pd.read_csv(os.path.join(BASE_DIR, "data", "ideal.csv"))

def load_test_data() -> pd.DataFrame:
    """Loads the test dataset with x-y pairs"""
    return pd.read_csv(os.path.join(BASE_DIR, "data", "test.csv"))

def get_data_paths():
    """Returns dictionary of absolute file paths used throughout the project"""
    return {
        "train": os.path.join(BASE_DIR, "data", "train1.csv"),
        "ideal": os.path.join(BASE_DIR, "data", "ideal.csv"),
        "test": os.path.join(BASE_DIR, "data", "test.csv"),
        "sqlite": os.path.join(BASE_DIR, "data", "function_mapping.db"),
    }
