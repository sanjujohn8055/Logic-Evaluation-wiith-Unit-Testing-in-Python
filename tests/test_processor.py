import pandas as pd
from src.processor import FunctionMapper, TestDataMapper
from src.loader import load_train_data, load_ideal_data, load_test_data
from src.exceptions import MappingException

train_df = load_train_data()
ideal_df = load_ideal_data()
test_df = load_test_data()

def test_find_best_fit_returns_four():
    mapper = FunctionMapper(train_df, ideal_df)
    matches = mapper.find_best_fit()
    assert len(matches) == 4
    for key, val in matches.items():
        assert key.startswith("y") and val.startswith("y")

def test_test_mapper_mapping_format():
    fm = FunctionMapper(train_df, ideal_df)
    matches = fm.find_best_fit()

    test_mapper = TestDataMapper(matches, train_df)
    result_df = test_mapper.map(test_df, ideal_df)

    assert not result_df.empty
    assert "ideal_function" in result_df.columns
    assert "deviation" in result_df.columns
