import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    student_count = courses.groupby('class')['student'].count()

    classes = student_count[student_count >= 5].index

    return pd.DataFrame(classes, columns=['class'])
