import pandas as pd

def load_clean_data():

    df = pd.read_csv("dataset.csv")

    df = df[[
        "studytime",
        "failures",
        "absences",
        "traveltime",
        "schoolsup",
        "famsup",
        "internet",
        "higher",
        "G1",
        "G2",
        "G3"
    ]]

    df = df.dropna()

    df["status"] = df["G3"].apply(
        lambda x: "ผ่าน" if x >= 10 else "เสี่ยงตก"
    )

    return df