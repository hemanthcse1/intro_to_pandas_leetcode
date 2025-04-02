import pandas as pd

def select_data(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ['name','age']]


data = {
    "student_id": [101, 53, 128, 3],
    "name": ["Ulysses", "William", "Henry", "Henry"],
    "age": [13, 10, 6, 11]
}

original_students = pd.DataFrame(data)

print(original_students)

print("***************************************")

result = select_data(original_students)

print(result)