import plotly.graph_objects as go
from data_handling import preprocess_data

def create_graph(df, variable):
    """Creates a Plotly line graph for the given variable."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['JaarKwartaal'],
        y=df[variable],
        mode='lines+markers',
        name=variable
    ))

    fig.update_layout(
        title=f'{variable} over Time',
        xaxis_title='Jaar Kwartaal',
        yaxis_title=variable,
        template='plotly_white',  # Use a clean template
        font=dict(family="Arial, sans-serif", size=12, color="#7f7f7f"),
    )

    # Convert to HTML, include plotly.js from a CDN, and make it standalone
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph_html