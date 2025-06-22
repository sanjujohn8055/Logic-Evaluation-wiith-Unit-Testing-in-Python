# # from loader import load_train_data, load_ideal_data
# # from processor import find_best_fit
# # from visualizer import plot_matches  # Optional

# # def main():
# #     train_df = load_train_data()
# #     ideal_df = load_ideal_data()

# #     matches = find_best_fit(train_df, ideal_df)

# #     print("\nBest fit mapping:")
# #     for train_col, ideal_col in matches.items():
# #         print(f"{train_col} --> {ideal_col}")

# #     # Optional: visualize results
# #     plot_matches(train_df, ideal_df, matches)
# # if __name__ == "__main__":
# #     main()
# from loader import load_train_data, load_ideal_data, load_test_data
# from processor import find_best_fit,map_test_data
# from visualizer import plot_matches, plot_test_matches

# def main():
#     train_df = load_train_data()
#     ideal_df = load_ideal_data()
#     test_df = load_test_data()

#     matches = find_best_fit(train_df, ideal_df)

#     print("\nBest fit mapping:")
#     for train_col, ideal_col in matches.items():
#         print(f"{train_col} --> {ideal_col}")

#     # Visualize training data vs best ideal matches
#     plot_matches(train_df, ideal_df, matches)

#     # Process and map test data
#     mapped_test_df = map_test_data(test_df, ideal_df, matches, train_df)

#     # Visualize mapped test data
#     plot_test_matches(mapped_test_df, ideal_df)

# if __name__ == "__main__":
#     main()

from loader import load_train_data, load_ideal_data, load_test_data, get_data_paths
from processor import FunctionMapper, TestDataMapper
from visualizer import plot_matches, plot_test_matches
from database import DatabaseHandler
import os


def main():
    # Load data
    train_df = load_train_data()
    ideal_df = load_ideal_data()
    test_df = load_test_data()

    # Step 1: Match training functions to ideal functions
    mapper = FunctionMapper(train_df, ideal_df)
    matches = mapper.find_best_fit()

    print("\nBest fit mapping:")
    for train_col, ideal_col in matches.items():
        print(f"{train_col} --> {ideal_col}")

    # Step 2: Visualize training to ideal function mappings
    plot_matches(train_df, ideal_df, matches)

    # Step 3: Map test data using only the selected 4 ideal functions
    test_mapper = TestDataMapper(matches, train_df)
    mapped_df = test_mapper.map(test_df, ideal_df)

    # Step 4: Visualize test data mapping
    plot_test_matches(mapped_df, ideal_df)

    # Step 5: Save to SQLite database
    sqlite_path = get_data_paths()["sqlite"]

    # ✅ Fix: ensure correct URL format for SQLAlchemy
    sqlite_url = f"sqlite:///{os.path.abspath(sqlite_path)}"

    db = DatabaseHandler(sqlite_url)
    db.save_to_db("train_data", train_df)
    db.save_to_db("ideal_functions", ideal_df)
    db.save_to_db("test_results", mapped_df)

    print("\n✅ Data saved to SQLite database.")


if __name__ == "__main__":
    main()
