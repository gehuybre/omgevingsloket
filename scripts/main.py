# /content/drive/MyDrive/Colab Notebooks/Vergunningen/scripts/main.py
from variables import TEMPLATE_FILE, OUTPUT_FILE, GRAPH_VARIABLES, TABLE_VARIABLES, STATIC_DIR
from data_handling import load_data, preprocess_data
from graph_generator import create_graph
from table_generator import create_table
import os

def main():
    """Generates the HTML report."""
    df = load_data()
    df = preprocess_data(df)

    graph_sections = ""
    for var in GRAPH_VARIABLES:
        graph_html = create_graph(df, var)
        table_html = create_table(df, var)
        placeholder_text = PLACEHOLDER_TEXTS.get(var, "")

        graph_sections += f"""
        <section class='parallax'>
            <div class='parallax-content'>
                <h2>{var}</h2>
                <div class='content-grid'>
                    <div class='text-column'>
                        {placeholder_text}
                    </div>
                    <div class='chart-table-column'>
                        <div class='chart'>{graph_html}</div>
                        {table_html}
                    </div>
                </div>
            </div>
        </section>
        """

    # Read the HTML template
    with open(TEMPLATE_FILE, 'r') as f:
        template_html = f.read()

    # Read the CSS file
    css_file = os.path.join(STATIC_DIR, 'styles.css')
    with open(css_file, 'r') as f:
        css_content = f.read()

    # Embed CSS into the template
    output_html = template_html.replace("</head>", f"<style>\n{css_content}\n</style>\n</head>")

    # Insert graph sections into the template
    output_html = output_html.replace("{{GRAPH_SECTIONS}}", graph_sections)

    # Write the output HTML
    with open(OUTPUT_FILE, 'w') as f:
        f.write(output_html)

    print(f"Report generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()