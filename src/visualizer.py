# # from bokeh.plotting import figure, show
# # from bokeh.layouts import column

# # def plot_matches(train_df, ideal_df, matches):
# #     plots = []

# #     for train_col, ideal_col in matches.items():
# #         p = figure(title=f"{train_col} vs {ideal_col}", width=600, height=300)
# #         p.line(train_df["x"], train_df[train_col], color="blue", legend_label=train_col)
# #         p.line(ideal_df["x"], ideal_df[ideal_col], color="red", legend_label=ideal_col, line_dash="dashed")
# #         plots.append(p)

# #     show(column(*plots))
# from bokeh.plotting import figure, show
# from bokeh.layouts import column

# def plot_matches(train_df, ideal_df, matches):
#     plots = []

#     for train_col, ideal_col in matches.items():
#         p = figure(title=f"{train_col} vs {ideal_col}", width=600, height=300)
#         p.line(train_df["x"], train_df[train_col], color="blue", legend_label=train_col)
#         p.line(ideal_df["x"], ideal_df[ideal_col], color="red", legend_label=ideal_col, line_dash="dashed")
#         plots.append(p)

#     show(column(*plots))

# def plot_test_matches(test_df, ideal_df):
#     plots = []
#     if "ideal_function" not in test_df.columns:
#         print("Test data has no mapped ideal functions to plot.")
#         return

#     for func in test_df["ideal_function"].unique():
#         sub_df = test_df[test_df["ideal_function"] == func]
#         ideal_y = ideal_df.set_index("x").loc[sub_df["x"], func].values

#         p = figure(title=f"Test Points mapped to {func}", width=600, height=300)
#         p.circle(sub_df["x"], sub_df["y"], color="green", size=6, legend_label="Test Data")
#         p.line(sub_df["x"], ideal_y, color="red", legend_label=f"Ideal: {func}", line_dash="dashed")
#         plots.append(p)

#     show(column(*plots))

from bokeh.plotting import figure, show
from bokeh.layouts import column


def plot_matches(train_df, ideal_df, matches):
    plots = []

    for train_col, ideal_col in matches.items():
        p = figure(title=f"{train_col} vs {ideal_col}", width=600, height=300)
        p.line(train_df["x"], train_df[train_col], color="blue", legend_label=train_col)
        p.line(ideal_df["x"], ideal_df[ideal_col], color="red", legend_label=ideal_col, line_dash="dashed")
        plots.append(p)

    show(column(*plots))


def plot_test_matches(mapped_df, ideal_df):
    plots = []

    for func in mapped_df["ideal_function"].unique():
        sub_df = mapped_df[mapped_df["ideal_function"] == func]
        ideal_y = ideal_df.set_index("x").loc[sub_df["x"], func].values

        p = figure(title=f"Test Points mapped to {func}", width=600, height=300)
        p.circle(sub_df["x"], sub_df["y"], color="green", size=6, legend_label="Test Data")
        p.line(sub_df["x"], ideal_y, color="red", legend_label=f"Ideal: {func}", line_dash="dashed")
        plots.append(p)

    show(column(*plots))


