from typing import List

import pandas as pd

def create_dataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])


student_data = [
    [101, 18],
    [102, 19],
    [103, 17],
    [104, 18],
    [105, 20],
    [106, 21],
    [107, 22],
    [108, 19],
    [109, 20],
    [110, 18]
]

result = create_dataframe(student_data)

print(result)