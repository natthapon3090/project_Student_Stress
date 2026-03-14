import dash
from dash import html, dcc
import plotly.graph_objects as go

from modules.data_cleaning import load_clean_data

dash.register_page(__name__, path="/analytics")

df = load_clean_data()
df = df.reset_index()


# -----------------------
# กราฟ 1 แนวโน้มคะแนน
# -----------------------
def score_chart(df):

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["index"],
        y=df["G3"],
        mode="lines",
        fill="tozeroy",
        name="คะแนนสอบ",
        line=dict(color="green", width=3)
    ))

    fig.update_layout(
        title="แนวโน้มคะแนนสอบ",
        xaxis_title="ลำดับข้อมูล",
        yaxis_title="คะแนน",
        height=450,
        template="plotly_white"
    )

    fig.update_xaxes(rangeslider_visible=True)

    return fig


# -----------------------
# กราฟ 2 เวลาอ่านหนังสือ
# -----------------------
def studytime_chart(df):

    data = df.sort_values("studytime")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["studytime"],
        y=data["G3"],
        mode="lines+markers",
        fill="tozeroy",
        name="คะแนน",
        line=dict(color="blue", width=3),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title="เวลาอ่านหนังสือกับคะแนน",
        xaxis_title="เวลาอ่านหนังสือ",
        yaxis_title="คะแนน",
        height=450,
        template="plotly_white"
    )

    fig.update_xaxes(rangeslider_visible=True)

    return fig


# -----------------------
# กราฟ 3 การขาดเรียน
# -----------------------
def absence_chart(df):

    data = df.sort_values("absences")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data["absences"],
        y=data["G3"],
        mode="lines+markers",
        fill="tozeroy",
        name="คะแนน",
        line=dict(color="red", width=3),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title="การขาดเรียนกับคะแนน",
        xaxis_title="จำนวนครั้งที่ขาดเรียน",
        yaxis_title="คะแนน",
        height=450,
        template="plotly_white"
    )

    fig.update_xaxes(rangeslider_visible=True)

    return fig


layout = html.Div(
    style={"padding": "30px"},
    children=[

        html.H2(
            "Dashboard วิเคราะห์ข้อมูลนักศึกษา",
            style={"textAlign": "center"}
        ),

        html.Div(
            dcc.Graph(figure=score_chart(df)),
            style={"marginBottom": "70px"}
        ),

        html.Div(
            dcc.Graph(figure=studytime_chart(df)),
            style={"marginBottom": "70px"}
        ),

        html.Div(
            dcc.Graph(figure=absence_chart(df))
        )

    ]
)
