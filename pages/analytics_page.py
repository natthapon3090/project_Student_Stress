import dash
from dash import html, dcc
from modules.data_cleaning import load_clean_data
from modules.charts import histogram_score, studytime_chart, absence_chart

dash.register_page(__name__, path="/analytics")

df = load_clean_data()

layout = html.Div(className="card", children=[

    html.H2("การวิเคราะห์ข้อมูลนักศึกษา"),

    dcc.Graph(figure=histogram_score(df)),

    dcc.Graph(figure=studytime_chart(df)),

    dcc.Graph(figure=absence_chart(df))

])