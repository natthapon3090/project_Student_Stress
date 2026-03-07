import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/model")

accuracy = 0.87

confusion = pd.DataFrame({
"Actual":["ผ่าน","ผ่าน","เสี่ยงตก","เสี่ยงตก"],
"Predicted":["ผ่าน","เสี่ยงตก","ผ่าน","เสี่ยงตก"],
"Value":[120,15,20,90]
})

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