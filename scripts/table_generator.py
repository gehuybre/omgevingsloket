# /content/drive/MyDrive/Colab Notebooks/Vergunningen/scripts/table_generator.py
import pandas as pd

def calculate_yty_percentage_change(df, variable):
    """Calculates the year-over-year percentage change for a given variable."""
    df_yearly = df.groupby('Jaar')[variable].sum().reset_index()
    df_yearly[f'{variable}_yty_change'] = df_yearly[variable].pct_change() * 100
    # Afronden van de berekende waardes:
    df_yearly[variable] = df_yearly[variable].round(0).astype(int) # Afronden naar 0 decimalen en converteren naar integer
    df_yearly[f'{variable}_yty_change'] = df_yearly[f'{variable}_yty_change'].round(0) # Rond YTY change af naar 0 decimalen
    return df_yearly

def create_table(df, variable):
    """Creates an HTML table for the given variable with yearly data and YTY change."""
    df_yearly = calculate_yty_percentage_change(df, variable)

    # Format the percentage change column. No need to round here anymore.
    df_yearly[f'{variable}_yty_change'] = df_yearly[f'{variable}_yty_change'].apply(lambda x: f'{x:.0f}%' if pd.notnull(x) else '')


    # Create the HTML table
    table_html = """
    <table class="data-table">
        <thead>
            <tr>
                <th>Year</th>
                <th>{}</th>
                <th>% verandering tov vorig jaar</th>
            </tr>
        </thead>
        <tbody>
    """.format(variable)

    for index, row in df_yearly.iterrows():
        table_html += f"""
            <tr>
                <td>{row['Jaar']}</td>
                <td>{row[variable]}</td>
                <td>{row[f'{variable}_yty_change']}</td>
            </tr>
        """

    table_html += """
        </tbody>
    </table>
    """
    return table_html