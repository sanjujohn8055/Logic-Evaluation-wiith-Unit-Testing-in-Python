# # import numpy as np
# # import pandas as pd

# # def find_best_fit(train_df, ideal_df):
# #     matches = {}
# #     for col in train_df.columns[1:]:  # Skip 'x'
# #         x_vals = train_df["x"]
# #         y_vals = train_df[col]
        
# #         min_error = float("inf")
# #         best_fit = None

# #         for ideal_col in ideal_df.columns[1:]:
# #             ideal_y = np.interp(x_vals, ideal_df["x"], ideal_df[ideal_col])
# #             error = np.sum((y_vals - ideal_y) ** 2)

# #             if error < min_error:
# #                 min_error = error
# #                 best_fit = ideal_col
        
# #         matches[col] = best_fit
# #     return matches
# import numpy as np
# import pandas as pd

# def find_best_fit(train_df, ideal_df):
#     matches = {}
#     for col in train_df.columns[1:]:  # Skip 'x'
#         x_vals = train_df["x"]
#         y_vals = train_df[col]
        
#         min_error = float("inf")
#         best_fit = None

#         for ideal_col in ideal_df.columns[1:]:
#             ideal_y = np.interp(x_vals, ideal_df["x"], ideal_df[ideal_col])
#             error = np.sum((y_vals - ideal_y) ** 2)

#             if error < min_error:
#                 min_error = error
#                 best_fit = ideal_col
        
#         matches[col] = best_fit

#     return matches  # ✅ Must be indented correctly
# def map_test_data(test_df, ideal_df, matches, train_df):
#     """
#     Maps each test (x, y) to the best matching ideal function
#     based on the lowest absolute deviation from the ideal function.
#     """
#     mapped_rows = []

#     for _, row in test_df.iterrows():
#         x_val = row["x"]
#         y_val = row["y"]

#         best_fit_func = None
#         min_deviation = float("inf")

#         for train_col, ideal_col in matches.items():
#             if x_val in ideal_df["x"].values:
#                 ideal_y = ideal_df.loc[ideal_df["x"] == x_val, ideal_col].values[0]
#                 deviation = abs(y_val - ideal_y)

#                 if deviation < min_deviation:
#                     min_deviation = deviation
#                     best_fit_func = ideal_col

#         mapped_rows.append({
#             "x": x_val,
#             "y": y_val,
#             "ideal_function": best_fit_func,
#             "deviation": min_deviation
#         })

#     return pd.DataFrame(mapped_rows)

# In src/processor.py

import numpy as np
import pandas as pd
from src.exceptions import MappingException


class FunctionMapper:
    """
    Finds the best-fitting ideal function for each training function based on minimal squared error.
    """

    def __init__(self, train_df: pd.DataFrame, ideal_df: pd.DataFrame):
        self.train_df = train_df
        self.ideal_df = ideal_df

    def find_best_fit(self):
        matches = {}
        for train_col in self.train_df.columns[1:]:  # Skip 'x'
            x_vals = self.train_df["x"]
            y_vals = self.train_df[train_col]

            min_error = float("inf")
            best_fit = None

            for ideal_col in self.ideal_df.columns[1:]:
                ideal_y = np.interp(x_vals, self.ideal_df["x"], self.ideal_df[ideal_col])
                error = np.sum((y_vals - ideal_y) ** 2)

                if error < min_error:
                    min_error = error
                    best_fit = ideal_col

            matches[train_col] = best_fit

        return matches


class TestDataMapper:
    """
    Maps test data to the best matching ideal function from previously selected ideal functions.
    """

    def __init__(self, matches: dict, train_df: pd.DataFrame):
        self.selected_ideals = list(matches.values())  # only top 4 ideal functions
        self.train_df = train_df

    def map(self, test_df: pd.DataFrame, ideal_df: pd.DataFrame) -> pd.DataFrame:
        mapped_results = []

        for _, row in test_df.iterrows():
            x = row["x"]
            y = row["y"]
            best_func = None
            min_deviation = float("inf")

            for ideal_col in self.selected_ideals:
                try:
                    ideal_value = np.interp(x, ideal_df["x"], ideal_df[ideal_col])
                    deviation = abs(y - ideal_value)

                    # Calculate threshold based on training max deviation
                    threshold = self._get_max_deviation(ideal_col, ideal_df)

                    if deviation <= threshold and deviation < min_deviation:
                        min_deviation = deviation
                        best_func = ideal_col

                except Exception as e:
                    raise MappingException(f"Error while mapping test point x={x}: {str(e)}")

            if best_func:
                mapped_results.append({
                    "x": x,
                    "y": y,
                    "ideal_function": best_func,
                    "deviation": min_deviation
                })

        return pd.DataFrame(mapped_results)

    def _get_max_deviation(self, ideal_col, ideal_df):
        # Estimate max deviation using training data vs ideal
        deviation_list = []

        for train_col in self.train_df.columns[1:]:
            if ideal_col not in ideal_df.columns:
                continue

            train_y = self.train_df[train_col]
            ideal_y = np.interp(self.train_df["x"], ideal_df["x"], ideal_df[ideal_col])
            deviation = np.abs(train_y - ideal_y)
            deviation_list.append(np.max(deviation))

        if deviation_list:
            return np.max(deviation_list) * np.sqrt(2)
        else:
            return float("inf")
