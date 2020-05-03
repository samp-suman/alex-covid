import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import plotly.express as px

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

world_confirmed=pd.read_csv('World_aggregate_data.csv')
location=world_confirmed['Country'].unique().tolist()
data = dict(type = 'choropleth',
            locations = location,
            z=world_confirmed['Confirmed'],
            locationmode = 'country names',
            colorscale= 'Portland',
            text= location,
            colorbar = {'title':'Country Colours', 'len':200,'lenmode':'pixels' })
layout = dict(geo = {'scope':'world'})
fig1=go.Figure(data=data,layout=layout)
fig1.update_layout(title={'text':"Worldwide Confirmed Cases",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},font=dict(family="Times New Roman,underline",size=15,color="#000000"))


rise_in_india=pd.read_csv('state_data_daybyday.csv')
fig2 = px.bar(rise_in_india, x="State", y="Confirmed",animation_group="State",animation_frame="Date",orientation='v')
fig2.update_xaxes(tickangle=50, tickfont=dict(family='Rockwell', color='crimson', size=10))
fig2.update_layout(title={'text':"Rise of Corona Cases in India",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},xaxis_title="States",yaxis_title="Confirmed Cases",font=dict(family="Times New Roman,underline",size=15,color="#000000"))


affected_countries=pd.read_csv('top_10_affected_countries.csv')
cols=['Country', 'Confirmed', 'Deaths', 'Recovered']
fig3= go.Figure(data=[go.Table(columnwidth = [29,25,19,20],header=dict(values=cols,fill_color='paleturquoise',align='left'),
                               cells=dict(values=[affected_countries.Country, affected_countries.Confirmed, affected_countries.Deaths, affected_countries.Recovered],fill_color='lavender',align='left'))
                      ])
fig3.update_layout(title={'text':"Top 10 Affected Countries",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},font=dict(family="Times New Roman,underline",size=15,color="#000000"))



india_stats = pd.read_csv('state_data_aggregate.csv')
cols=['State', 'Confirmed', 'Deaths', 'Recovered']
fig4= go.Figure(data=[go.Table(columnwidth = [29,24,18,20],header=dict(values=cols,fill_color='paleturquoise',align='left'),
                    cells=dict(values=[india_stats.State, india_stats.Confirmed, india_stats.Deaths, india_stats.Recovered],fill_color='lavender',align='left'))
                    ])
fig4.update_layout(title={'text':"Total Cases by States",'y':0.9,'x':0.5,'xanchor': 'center','yanchor': 'top'},font=dict(family="Times New Roman,underline",size=15,color="#000000"))



app=dash.Dash(__name__,external_stylesheets=external_stylesheets)
server=app.server

app.layout=html.Div([
    html.H1('COVID-19 Statistics', style={'color':'#FFFF00','text-align':'center','size':20}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(children=[dcc.Graph(id='World Cases Distribution',figure=fig1)])
                    ])
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(children=[dcc.Graph(id='India',figure=fig2)])
                    ])
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row'),
    html.Div([
        html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div(children=[dcc.Graph(id='top10',figure=fig3)])
                        ])
                    ],className='card-body')
                ],className='card')
        ],className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.Div(children=[dcc.Graph(id='Tally of India',figure=fig4)])
                    ])
                ],className='card-body')
            ],className='card')
        ],className='col-md-6')
    ],className='row')
],className='container')


if __name__=='__main__':
    app.run_server(debug=True)