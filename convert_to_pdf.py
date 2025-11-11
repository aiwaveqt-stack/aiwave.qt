#!/usr/bin/env python3
"""
Convert Markdown Report to PDF
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def convert_markdown_to_pdf(markdown_file, pdf_file):
    """Convert a markdown file to PDF with proper styling"""

    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )

    # Add CSS styling for better PDF appearance
    css_style = """
    @page {
        size: A4;
        margin: 2cm;
    }

    body {
        font-family: 'Arial', 'Helvetica', sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 100%;
    }

    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
        font-size: 28px;
    }

    h2 {
        color: #34495e;
        border-bottom: 2px solid #95a5a6;
        padding-bottom: 8px;
        margin-top: 25px;
        font-size: 22px;
    }

    h3 {
        color: #2c3e50;
        margin-top: 20px;
        font-size: 18px;
    }

    h4 {
        color: #34495e;
        margin-top: 15px;
        font-size: 16px;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin: 15px 0;
        font-size: 11px;
    }

    th {
        background-color: #3498db;
        color: white;
        padding: 10px;
        text-align: left;
        font-weight: bold;
    }

    td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    code {
        background-color: #f4f4f4;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 10px;
    }

    pre {
        background-color: #f8f8f8;
        border: 1px solid #ddd;
        border-left: 4px solid #3498db;
        padding: 10px;
        overflow-x: auto;
        font-size: 10px;
        line-height: 1.4;
    }

    pre code {
        background-color: transparent;
        padding: 0;
    }

    blockquote {
        border-left: 4px solid #3498db;
        padding-left: 15px;
        margin-left: 0;
        color: #666;
        font-style: italic;
    }

    ul, ol {
        margin: 10px 0;
        padding-left: 30px;
    }

    li {
        margin: 5px 0;
    }

    hr {
        border: none;
        border-top: 2px solid #3498db;
        margin: 30px 0;
    }

    .winner {
        color: #27ae60;
        font-weight: bold;
    }

    .emoji {
        font-size: 1.2em;
    }

    a {
        color: #3498db;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    strong {
        color: #2c3e50;
    }
    """

    # Create full HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Repository Comparison Report</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    print(f"Converting {markdown_file} to PDF...")
    HTML(string=full_html).write_pdf(
        pdf_file,
        stylesheets=[CSS(string=css_style)]
    )
    print(f"✓ PDF generated successfully: {pdf_file}")

if __name__ == "__main__":
    markdown_file = "/home/user/aiwave.qt/REPOSITORY_COMPARISON_REPORT.md"
    pdf_file = "/home/user/aiwave.qt/REPOSITORY_COMPARISON_REPORT.pdf"

    convert_markdown_to_pdf(markdown_file, pdf_file)
