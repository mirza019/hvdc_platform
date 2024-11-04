# dashboard.py
from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# Sample data for initial visualization
data = pd.DataFrame({
    'Time': pd.date_range(start="2024-01-01", periods=100, freq="H"),
    'Voltage': np.random.normal(500, 10, 100),
    'Current': np.random.normal(1.5, 0.1, 100)
})

# Create dashboard layout
dash_app.layout = html.Div([
    dcc.Graph(
        id='voltage-current-trend',
        figure={
            'data': [
                go.Scatter(x=data['Time'], y=data['Voltage'], mode='lines', name='Voltage'),
                go.Scatter(x=data['Time'], y=data['Current'], mode='lines', name='Current')
            ],
            'layout': go.Layout(title='Voltage and Current Trend')
        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
