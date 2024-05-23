"""
Filter the DataFrame to select people younger than 26
"""

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}
df = pd.DataFrame(data)
print(df)
