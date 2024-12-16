import pandas as pd

def view_attendance():
    df = pd.read_csv("attendance.csv", names=["Name", "Timestamp"])
    print(df)

# Usage
view_attendance()
