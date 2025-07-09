from src.data_loading import load_input_data
import os

def test_load_csv():
    filepath = "data/inputs/sample.csv"
    if os.path.exists(filepath):
        df = load_input_data(filepath)
        assert not df.empty