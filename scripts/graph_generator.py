# /content/drive/MyDrive/Colab Notebooks/Vergunningen/scripts/graph_generator.py
import plotly.graph_objects as go
from data_handling import preprocess_data
from variables import TITLES  # Importeer de TITLES dictionary

def create_graph(df, variable):
    """Creates a Plotly line graph for the given variable."""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['JaarKwartaal'],
        y=df[variable],
        mode='lines+markers',
        name=variable
    ))

    # Gebruik de TITLES dictionary om de titel op te halen
    title_text = TITLES.get(variable, variable)  # Fallback naar variable als de titel niet gevonden is

    fig.update_layout(
        title=title_text,  # Gebruik de opgehaalde titel
        xaxis_title='Jaar Kwartaal',
        yaxis_title=variable,
        template='plotly_white',
        font=dict(family="Arial, sans-serif", size=12, color="#7f7f7f"),
        # Make the background transparent
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
    )
    # Remove grid lines
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Convert to HTML, include plotly.js from a CDN, and make it standalone
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph_html