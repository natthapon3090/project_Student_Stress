import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

from modules.prediction import predict_risk
from modules.recommendation import recommend

dash.register_page(__name__, path="/")

layout = html.Div(className="row", children=[

    html.Div(className="card column", children=[

        html.H3("แบบประเมินนักศึกษา"),

        html.Label("ชั่วโมงเรียนต่อสัปดาห์"),
        dcc.Slider(1,4,1,value=2,id="studytime"),

        html.Label("จำนวนครั้งที่ตกวิชา"),
        dcc.Slider(0,4,1,value=0,id="failures"),

        html.Label("จำนวนครั้งขาดเรียน"),
        dcc.Slider(0,100,1,value=5,id="absences"),

        html.Label("เวลาเดินทางเรียน(นาที)"),
        dcc.Slider(1,60,1,value=1,id="traveltime"),

        html.Label("คะแนนกลางภาค"),
        dcc.Slider(0,20,1,value=10,id="G1"),

        html.Label("คะแนนก่อนสอบปลายภาค"),
        dcc.Slider(0,20,1,value=10,id="G2"),

        html.Br(),

        html.Button("พยากรณ์", id="btn", className="button-main"),

        html.Div(id="result", style={"marginTop":"10px","fontWeight":"bold"}),
        html.Div(id="recommend")

    ]),

    html.Div(className="card column", children=[

        html.H3("ระดับความเสี่ยง"),

        dcc.Graph(id="gauge")

    ])
])


@dash.callback(
    [Output("result","children"),
     Output("recommend","children"),
     Output("gauge","figure")],

    Input("btn","n_clicks"),

    State("studytime","value"),
    State("failures","value"),
    State("absences","value"),
    State("traveltime","value"),
    State("G1","value"),
    State("G2","value"),

    prevent_initial_call=True
)

def predict(n,studytime,failures,absences,traveltime,G1,G2):

    data={
        "studytime":[studytime],
        "failures":[failures],
        "absences":[absences],
        "traveltime":[traveltime],
        "schoolsup":["no"],
        "famsup":["yes"],
        "internet":["yes"],
        "higher":["yes"],
        "G1":[G1],
        "G2":[G2]
    }

    result,prob=predict_risk(data)

    # แปลง probability ให้เป็นระดับความเสี่ยงจริง
    if result == "เสี่ยงตก":
        value = prob * 100
    else:
        value = (1 - prob) * 100

    value = round(value,2)

    gauge=go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text":"ระดับความเสี่ยง (%)"},
        gauge={
            "axis":{"range":[0,100]},
            "steps":[
                {"range":[0,40],"color":"green"},
                {"range":[40,70],"color":"orange"},
                {"range":[70,100],"color":"red"}
            ]
        }
    ))

    return f"ผลการพยากรณ์ : {result}", recommend(result), gauge