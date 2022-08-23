import dash
import dash_html_components as html
import dash_pivottable

import pandas as pd

app = dash.Dash(__name__)
app.title = '2022 Russia Ukraine War'

data = pd.read_csv('./russia_losses_equipment.csv')

app.layout = html.Div([
    dash_pivottable.PivotTable(
        id='table',
        data=data.to_dict('records'),
        #cols=data.columns,
        #colOrder="key_a_to_z",
        #rows=['Party Size'],
        #rowOrder="key_a_to_z",
        #rendererName="Grouped Column Chart",
        #aggregatorName="Average",
        #vals=["Total Bill"],
        #valueFilter={'Day of Week': {'Thursday': False}}
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)