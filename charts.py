import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


def radar_chart(
    keyword_score,
    ai_score,
    skill_match
):

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=[
                keyword_score,
                ai_score,
                skill_match
            ],
            theta=[
                "Keyword",
                "AI",
                "Skills"
            ],
            fill="toself"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        )
    )

    return fig


def skill_match_chart(
    matched_count,
    missing_count
):

    df = pd.DataFrame({

        "Category": [
            "Matched",
            "Missing"
        ],

        "Count": [
            matched_count,
            missing_count
        ]
    })

    fig = px.bar(
        df,
        x="Category",
        y="Count"
    )

    return fig