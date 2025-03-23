from dash import Dash, html, dcc, Input, Output, State, callback_context, ALL  # Added ALL here
import plotly.express as px
import psutil
from collections import deque
import time
from threading import Thread

app = Dash(__name__)

# Initialize data structures
cpu_data = deque(maxlen=50)
memory_data = deque(maxlen=50)
timestamps = deque(maxlen=50)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Real-Time System Monitoring Dashboard"),
    dcc.Graph(id='cpu-usage-graph'),
    dcc.Graph(id='memory-usage-graph'),
    html.H3("Running Processes"),
    html.Div(id='process-table'),
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
])

# Function to update CPU and memory data
def update_data():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        timestamps.append(time.strftime("%H:%M:%S"))
        cpu_data.append(cpu_usage)
        memory_data.append(memory_usage)
        time.sleep(2)

# Start the data update thread
Thread(target=update_data, daemon=True).start()

# Callback to update the graphs and process table
@app.callback(
    [Output('cpu-usage-graph', 'figure'),
     Output('memory-usage-graph', 'figure'),
     Output('process-table', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    # Update CPU and Memory graphs
    cpu_fig = px.line(x=list(timestamps), y=list(cpu_data), labels={'x': 'Time', 'y': 'CPU Usage (%)'}, title="CPU Usage Over Time")
    memory_fig = px.line(x=list(timestamps), y=list(memory_data), labels={'x': 'Time', 'y': 'Memory Usage (%)'}, title="Memory Usage Over Time")
    
    # Update process table
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(html.Tr([
            html.Td(proc.info['pid']),
            html.Td(proc.info['name']),
            html.Td(f"{proc.info['cpu_percent']:.2f}%"),
            html.Td(f"{proc.info['memory_percent']:.2f}%"),
            html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0))
        ]))
    
    process_table = html.Table([
        html.Thead(html.Tr([html.Th("PID"), html.Th("Name"), html.Th("CPU (%)"), html.Th("Memory (%)"), html.Th("Action")])),
        html.Tbody(processes)
    ])
    
    return cpu_fig, memory_fig, process_table

# Callback to handle kill button clicks
@app.callback(
    Output('process-table', 'children', allow_duplicate=True),
    Input({'type': 'kill-btn', 'index': ALL}, 'n_clicks'),  # Fixed: Replaced dash.ALL with ALL
    prevent_initial_call=True
)
def kill_process(n_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update
    
    # Get the PID from the button ID
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    pid = int(button_id.split(':')[-1].strip('}"'))
    
    try:
        # Kill the process
        psutil.Process(pid).terminate()
    except psutil.NoSuchProcess:
        pass
    
    # Return the updated process table
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        processes.append(html.Tr([
            html.Td(proc.info['pid']),
            html.Td(proc.info['name']),
            html.Td(f"{proc.info['cpu_percent']:.2f}%"),
            html.Td(f"{proc.info['memory_percent']:.2f}%"),
            html.Td(html.Button('Kill', id={'type': 'kill-btn', 'index': proc.info['pid']}, n_clicks=0))
        ]))
    
    return html.Table([
        html.Thead(html.Tr([html.Th("PID"), html.Th("Name"), html.Th("CPU (%)"), html.Th("Memory (%)"), html.Th("Action")])),
        html.Tbody(processes)
    ])

if __name__ == "__main__":
    app.run(debug=True)
