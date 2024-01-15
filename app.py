import dash 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div ([
    html.H1("River"),
    html.Video(
        src="url.m3u8",
        controls=True,
        autoPlay=True,
        style= { "width": "100%"}
    )  
])

if __name__ == "__main__":
    app.run_server(debug=True)