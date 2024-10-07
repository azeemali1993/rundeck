import pandas as pd
from datetime import date

date_run =  date(day=30, month=11, year=2014).strftime('%A %d %B %Y')
# Sample DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})

df2 = pd.DataFrame({
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor'],
    'Price': [1200, 500, 800, 300],
    'Quantity': [50, 30, 100, 75]
})

df3 = pd.DataFrame({
    'Country': ['USA', 'France', 'Germany', 'UK'],
    'Capital': ['Washington', 'Paris', 'Berlin', 'London'],
    'Population (millions)': [331, 67, 83, 66]
})

# Convert DataFrames to HTML tables
html_df1 = df1.to_html(index=False, classes='dataframe')
html_df2 = df2.to_html(index=False, classes='dataframe')
html_df3 = df3.to_html(index=False, classes='dataframe')

# Create a complete HTML file with CSS for a modern design and collapsible functionality
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f0f4f8;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            color: #34495e;
        }}
        table.dataframe {{
            border-collapse: collapse;
            width: 80%;
            margin: 20px auto;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }}
        table.dataframe th, table.dataframe td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}
        table.dataframe th {{
            background-color: #3498db;
            color: white;
            text-align: left;
            padding-top: 12px;
            padding-bottom: 12px;
        }}
        table.dataframe td {{
            text-align: left;
        }}
        .container {{
            margin: 20px auto;
            width: 80%;
        }}
        .table-title {{
            font-size: 1.5rem;
            color: #2980b9;
            margin: 10px 0;
            text-align: center;
            cursor: pointer;
        }}
        .table-title:hover {{
            color: #1abc9c;
        }}
        .collapsible {{
            display: none;
            transition: display 0.3s ease;
        }}
    </style>
    <title>Collapsible DataFrames</title>
    <script>
        function toggleTable(tableId) {{
            var table = document.getElementById(tableId);
            if (table.style.display === "none" || table.style.display === "") {{
                table.style.display = "block";
            }} else {{
                table.style.display = "none";
            }}
        }}
    </script>
</head>
<body>
    <h1>Data Load Report <br>{date_run}</h1>

    <div class="container">
        <div class="table-title" onclick="toggleTable('table1')">DataFrame 1: People Information</div>
        <div id="table1" class="collapsible">{html_df1}</div>
    </div>

    <div class="container">
        <div class="table-title" onclick="toggleTable('table2')">DataFrame 2: Product Inventory</div>
        <div id="table2" class="collapsible">{html_df2}</div>
    </div>

    <div class="container">
        <div class="table-title" onclick="toggleTable('table3')">DataFrame 3: Country Information</div>
        <div id="table3" class="collapsible">{html_df3}</div>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open('collapsible_dataframes.html', 'w') as file:
    file.write(html_content)

print("Collapsible HTML file generated successfully!")
