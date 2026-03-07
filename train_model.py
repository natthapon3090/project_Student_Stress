import pandas as pd
from pycaret.classification import *

print("Loading dataset...")

df = pd.read_csv("dataset.csv")

# ใช้เฉพาะ feature ที่ dashboard ใช้
df = df[
[
"studytime",
"failures",
"absences",
"traveltime",
"G1",
"G2",
"G3"
]
]

# สร้าง target
df["status"] = df["G3"].apply(
lambda x: "ผ่าน" if x >= 10 else "เสี่ยงตก"
)

df = df.drop(columns=["G3"])

setup(
data=df,
target="status",
session_id=123,
normalize=True,
verbose=False
)

best_model = compare_models()

final_model = finalize_model(best_model)

save_model(final_model,"model_programming")

print("Model created successfully")