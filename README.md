# Data Quality Reporter

Python tool for checking data quality in CSV files and sending results via email.

## Quick Start

1. Fill in `configs/example_config.yaml` to match your data.
2. Update `main.py` with your email settings.
3. Run:

```bash
pip install -r requirements.txt
python main.py

#### `tests/test_checker.py`
```python
import pandas as pd
from data_quality.checker import check_not_null

def test_check_not_null():
    df = pd.DataFrame({
        'id': [1, None, 3],
        'name': ['A', None, 'C'],
        'age': [20, 30, None]
    })
    result = check_not_null(df, ['id', 'name', 'age'])
    assert result == {'id': 1, 'name': 1, 'age': 1}

Route	       Method	Protection	Description
/register	POST	None	        User sign-up
/login	        POST	None	        User login, get JWT
/protected-data	GET	JWT required	Accessible only with token
