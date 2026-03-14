import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

dash.register_page(__name__, path="/model")

# โหลด dataset
df = pd.read_csv("dataset.csv")

# เลือก feature
X = df[["studytime","failures","absences","traveltime","G1","G2"]]

# สร้าง target
y = df["G3"].apply(lambda x: "ผ่าน" if x >= 10 else "เสี่ยงตก")

# แบ่ง train / test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# สร้างโมเดล
model = RandomForestClassifier(n_estimators=200, random_state=42)

# train โมเดล
model.fit(X_train, y_train)

# ทำนายผล
y_pred = model.predict(X_test)

# คำนวณ accuracy จริง
accuracy = accuracy_score(y_test, y_pred)

# สร้าง confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=["ผ่าน","เสี่ยงตก"])

confusion = pd.DataFrame(
    cm,
    index=["Actual ผ่าน","Actual เสี่ยงตก"],
    columns=["Predicted ผ่าน","Predicted เสี่ยงตก"]
).reset_index().melt(id_vars="index")

confusion.columns = ["Actual","Predicted","Value"]

fig_confusion = px.density_heatmap(
    confusion,
    x="Actual",
    y="Predicted",
    z="Value",
    title="Confusion Matrix"
)

layout = html.Div(className="card", children=[

    html.H2("ประสิทธิภาพโมเดล Machine Learning"),

    html.H3(f"Accuracy : {accuracy*100:.2f}%"),

    dcc.Graph(figure=fig_confusion)

])
