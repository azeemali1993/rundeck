import pandas as pd

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

# HTML content with functional search
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
        }}
        .search-input {{
            display: block;
            margin: 10px auto;
            padding: 8px;
            width: 60%;
            border: 1px solid #ccc;
            border-radius: 4px;
        }}
    </style>
    <title>Search Feature for Tables</title>
    <script>
        // Function to search and filter table rows
        function searchTable(inputId, tableId) {{
            const input = document.getElementById(inputId);
            const filter = input.value.toUpperCase();  // Case-insensitive search
            const table = document.getElementById(tableId);
            const rows = table.getElementsByTagName("tr");

            // Loop through all table rows (excluding header row)
            for (let i = 1; i < rows.length; i++) {{
                let rowVisible = false;
                const cells = rows[i].getElementsByTagName("td");

                // Loop through all cells in a row
                for (let j = 0; j < cells.length; j++) {{
                    const cell = cells[j];
                    if (cell) {{
                        // Check if any cell contains the search term
                        if (cell.textContent.toUpperCase().indexOf(filter) > -1) {{
                            rowVisible = true;
                            break;  // Stop checking other cells in the same row
                        }}
                    }}
                }}
                // Show or hide the row based on the match
                rows[i].style.display = rowVisible ? "" : "none";
            }}
        }}
    </script>
</head>
<body>
    <h1>Data Report with Search Feature</h1>

    <div class="container">
        <div class="table-title">DataFrame 1: People Information (No Search)</div>
        <table id="table1-data" class="dataframe">{html_df1}</table>
    </div>

    <div class="container">
        <div class="table-title">DataFrame 2: Product Inventory (Search Enabled)</div>
        <input type="text" id="search-table2" class="search-input" onkeyup="searchTable('search-table2', 'table2-data')" placeholder="Search Table 2">
        <table id="table2-data" class="dataframe">{html_df2}</table>
    </div>

    <div class="container">
        <div class="table-title">DataFrame 3: Country Information (Search Enabled)</div>
        <input type="text" id="search-table3" class="search-input" onkeyup="searchTable('search-table3', 'table3-data')" placeholder="Search Table 3">
        <table id="table3-data" class="dataframe">{html_df3}</table>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open('working_search_filter.html', 'w') as file:
    file.write(html_content)

print("HTML file with working search filter generated successfully!")
