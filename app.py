import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True
)

app.layout = html.Div(className="container", children=[

    html.H1("ระบบพยากรณ์ความเสี่ยงการตกวิชา Programming",
            className="title"),

    html.Div([
        dcc.Link("หน้าแบบประเมิน", href="/", className="nav-btn"),
        dcc.Link("หน้า Data Analytics", href="/analytics", className="nav-btn"),
        dcc.Link("หน้า Model Performance", href="/model", className="nav-btn")
    ]),

    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)