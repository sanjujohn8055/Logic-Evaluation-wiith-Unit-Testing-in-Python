import os
from src.loader import load_train_data, load_ideal_data, load_test_data, get_data_paths

def test_load_train_data():
    df = load_train_data()
    assert not df.empty
    assert "x" in df.columns

def test_load_ideal_data():
    df = load_ideal_data()
    assert not df.empty
    assert "x" in df.columns
    assert len(df.columns) == 51  # 50 ideal + 1 x

def test_load_test_data():
    df = load_test_data()
    assert not df.empty
    assert "x" in df.columns
    assert "y" in df.columns

def test_data_paths_exist():
    paths = get_data_paths()
    for path in paths.values():
        assert os.path.exists(path)
