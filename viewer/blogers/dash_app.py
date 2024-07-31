from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
from django_loguru.middleware import logger

from .models import Bloger, Blog, Post, Comment
from logs.models import Logs, SpaceType, EventType

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css"

data = {
    "User Login": [],
    "Post Header": [],
    "Post Author Login": [],
    "Number of Comments": [],
}

data_logs = {
    "Date": [],
    "Login count": [],
    "Logout count": [],
    "Event count inside blog": [],
}

df = pd.DataFrame(data)
dfl = pd.DataFrame(data_logs)

app = DjangoDash("TableBlogerView", add_bootstrap_links=True, external_stylesheets=[dbc.themes.COSMO, dbc_css])

app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(dbc.Col(html.H1("Users Info", className="text-center my-4"), width=12)),
                dbc.Row(
                    [
                        dbc.Col(dbc.Input(id="nickname", placeholder="Enter user login", className="mb-2"), width=6),
                        dbc.Col(
                            dbc.Button("Fetch Data", id="button-fetch", color="primary", className="mb-2"), width=2
                        ),
                    ],
                    className="justify-content-center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dash_table.DataTable(
                                id="table-bloger-view",
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict("records"),
                                style_table={"height": "300px", "overflowY": "auto"},
                                style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
                                style_cell={
                                    "backgroundColor": "rgb(50, 50, 50)",
                                    "color": "white",
                                    "textAlign": "center",
                                    "padding": "10px",
                                },
                                export_format="csv",
                            ),
                            width=12,
                        ),
                    ],
                    className="mb-4",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dash_table.DataTable(
                                id="table-logs-view",
                                columns=[{"name": i, "id": i} for i in dfl.columns],
                                data=dfl.to_dict("records"),
                                style_table={"height": "300px", "overflowY": "auto"},
                                style_header={"backgroundColor": "rgb(30, 30, 30)", "color": "white"},
                                style_cell={
                                    "backgroundColor": "rgb(50, 50, 50)",
                                    "color": "white",
                                    "textAlign": "center",
                                    "padding": "10px",
                                },
                                style_data_conditional=[
                                    {
                                        "if": {"row_index": "odd"},
                                        "backgroundColor": "rgb(60, 60, 60)",
                                    }
                                ],
                                export_format="csv",
                            ),
                            width=12,
                        ),
                    ],
                ),
            ]
        )
    ]
)


@app.callback(
    Output("table-bloger-view", "data"),
    Output("table-logs-view", "data"),
    [Input("button-fetch", "n_clicks")],
    [State("nickname", "value")],
    prevent_initial_call=True,
)
def some(n_click, input_field):
    bloger = Bloger.objects.filter(login=input_field).first()
    if not bloger:
        logger.debug(f"Пользователя с ником: {input_field} не существует")
        return df.to_dict("records"), dfl.to_dict("records")

    bloger_id = bloger.id

    comments = Comment.objects.filter(author_id=bloger_id)
    post_ids = comments.values_list("post_id", flat=True)
    posts = Post.objects.filter(id__in=post_ids)

    date_logs = Logs.objects.filter(user_id=bloger_id)
    if not date_logs.exists():
        logger.debug(f"Пользователь с ником: {input_field} не осуществлял действий")

    event_login = EventType.objects.get(name="login")
    event_logout = EventType.objects.get(name="logout")
    event_blog = SpaceType.objects.get(name="blog")

    data = []
    data_logs = []

    for post in posts:
        post_author_login = post.author_id.login
        post_header = post.header
        num_comments = comments.filter(post_id=post.id).count()

        data.append(
            {
                "User Login": input_field,
                "Post Header": post_header,
                "Post Author Login": post_author_login,
                "Number of Comments": num_comments,
            }
        )

    for log in date_logs:
        date = log.datetime.date()
        login_count = date_logs.filter(event_type_id=event_login, datetime__date=date).count()
        logout_count = date_logs.filter(event_type_id=event_logout, datetime__date=date).count()
        event_blog_count = date_logs.filter(space_type_id=event_blog, datetime__date=date).count()

        data_logs.append(
            {
                "Date": date,
                "Login count": login_count,
                "Logout count": logout_count,
                "Event count inside blog": event_blog_count,
            }
        )

    return pd.DataFrame(data).to_dict("records"), pd.DataFrame(data_logs).to_dict("records")
