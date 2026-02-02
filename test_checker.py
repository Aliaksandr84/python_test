import pandas as pd
from data_quality.checker import check_not_null

def test_check_not_null_no_missing():
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 35]
    })
    result = check_not_null(df, ['id', 'name', 'age'])
    assert result == {'id': 0, 'name': 0, 'age': 0}

def test_check_not_null_with_missing():
    df = pd.DataFrame({
        'id': [1, None, 3],
        'name': ['Alice', None, 'Charlie'],
        'age': [30, 25, None]
    })
    result = check_not_null(df, ['id', 'name', 'age'])
    assert result == {'id': 1, 'name': 1, 'age': 1}