#!/usr/bin/python
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from datetime import timedelta

errors = pd.read_csv('azure-data/PdM_errors.csv')
failures = pd.read_csv('azure-data/PdM_failures.csv')
machines = pd.read_csv('azure-data/PdM_machines.csv')
inspections = pd.read_csv('azure-data/PdM_maint.csv')
telemetry = pd.read_csv('azure-data/PdM_telemetry.csv')

errors['datetime_dt'] = pd.to_datetime(errors.datetime)
failures['datetime_dt'] = pd.to_datetime(failures.datetime)
inspections['datetime_dt'] = pd.to_datetime(inspections.datetime)
telemetry['datetime_dt'] = pd.to_datetime(telemetry.datetime)

default_start_date = min(telemetry.datetime_dt)
max_end_date = max(telemetry.datetime_dt)
default_end_date = default_start_date + timedelta(days=2)

machine_dropdown_options = [{'label': f'machine {i}', 'value': i} for i in machines.machineID]
machine_dropdown_default = machines.machineID[0]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Date Selector'),
    html.Br(),
    dcc.DatePickerRange(id='my-date-picker-range',
                        min_date_allowed=default_start_date,
                        max_date_allowed=max_end_date,
                        end_date=default_end_date,
                        start_date=default_start_date),
    html.Br(),
    html.Label('Machine Selector'),
    dcc.Dropdown(id='machine-selector',
                 options=machine_dropdown_options,
                 value=[machine_dropdown_default], multi=True),
    html.Br(),
    dcc.Graph(id='telemetry-chart'),
    ])


@app.callback(Output('telemetry-chart', 'figure'),
              [Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date'),
              Input('machine-selector', 'value')])
def update_figure(start, end, selected_machines):
    print('start-end ', start, end)
    print(machines)

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    query = """
        datetime_dt > @start and \
        datetime_dt < @end and \
        machineID in @selected_machines \
    """

    filtered_telemetry = telemetry.query(query)

    # print(filtered_telemetry)

    data = []
    for c in filtered_telemetry.columns[2:]:
        trace = go.Scattergl(x=filtered_telemetry['datetime'],
                             y=filtered_telemetry[c], mode='markers',
                             name=c)
        data.append(trace)

    layout = go.Layout(title='Telemetry')

    fig = go.Figure(data=data, layout=layout)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
