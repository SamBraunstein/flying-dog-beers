import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server=app.server

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.title = 'Deloitte Dash'

app.layout = html.Div(children=[
    html.H1('Late Stage tech startups are raising more private capital'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['2016', '2017', '2018'], 'y': [16, 12, 28], 'type': 'bar', 'name': 'Private: 100MM+ VC Capital'},
                {'x': ['2016', '2017', '2018'], 'y': [3, 6, 5], 'type': 'bar', 'name': 'Public: IPO Public Capital'},
            ],
            'layout': {
                'title': "Private ($100MM+ US VC Rounds) versus Public (US IPOs)",
                'xaxis':{'title':'Trend 2016 through 2018, Source: Pitchbook 4Q 2018'},
                'yaxis':{'title':'Investments in companies, $ in Billions'},
            }
        }
    )]
)

if __name__ == '__main__':
    app.run_server()
