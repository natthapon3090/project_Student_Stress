import plotly.express as px

def histogram_score(df):

    fig = px.histogram(
        df,
        x="G3",
        nbins=20,
        title="การกระจายคะแนนสอบปลายภาค"
    )

    return fig


def studytime_chart(df):

    data = df.groupby("studytime")["G3"].mean().reset_index()

    fig = px.bar(
        data,
        x="studytime",
        y="G3",
        title="ค่าเฉลี่ยคะแนนตามชั่วโมงเรียน"
    )

    return fig


def absence_chart(df):

    fig = px.scatter(
        df,
        x="absences",
        y="G3",
        title="ความสัมพันธ์ระหว่างการขาดเรียนกับคะแนน"
    )

    return fig