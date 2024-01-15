import dash 
import dash_html_components as html 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("River")
    html.Video(
        src="url.m3u8",
        controls = True,
        autoplay= True,
        style= { "width"= "100%"}
    )
    
])