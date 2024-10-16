import pandas as pd

# Create three example DataFrames
data1 = {'Name': ['John', 'Jane', 'Tom'],
         'Age': [28, 24, 35],
         'Occupation': ['Engineer', 'Doctor', 'Teacher']}

data2 = {'Product': ['Apple', 'Banana', 'Cherry'],
         'Price': [1.2, 0.5, 2.5],
         'Stock': [100, 150, 80]}

data3 = {'City': ['New York', 'Los Angeles', 'Chicago'],
         'Population': [8419600, 3980400, 2716000],
         'Area': [789, 503, 589]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
table1 = df1.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table1')
table2 = df2.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table2')
table3 = df3.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table3')


# HTML template with Bootstrap and search functionality
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DataFrames to HTML Tables</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {{
            padding: 20px;
        }}
        .search-box {{
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>

    <h2>DataFrame 1</h2>
    <input class="form-control search-box" type="text" id="search1" onkeyup="searchTable(1)" placeholder="Search for anything...">
    {table1}

    <h2>DataFrame 2</h2>
    <input class="form-control search-box" type="text" id="search2" onkeyup="searchTable(2)" placeholder="Search for anything...">
    {table2}

    <h2>DataFrame 3</h2>
    <input class="form-control search-box" type="text" id="search3" onkeyup="searchTable(3)" placeholder="Search for anything...">
    {table3}

    <script>
        function searchTable(tableNum) {{
            let input = document.getElementById('search' + tableNum);
            let filter = input.value.toLowerCase();
            let table = document.getElementById('table' + tableNum);
            let tr = table.getElementsByTagName('tr');

            for (let i = 1; i < tr.length; i++) {{
                let row = tr[i];
                let tds = row.getElementsByTagName('td');
                let found = false;

                for (let j = 0; j < tds.length; j++) {{
                    if (tds[j]) {{
                        if (tds[j].innerText.toLowerCase().indexOf(filter) > -1) {{
                            found = true;
                            break;
                        }}
                    }}
                }}

                if (found) {{
                    tr[i].style.display = '';
                }} else {{
                    tr[i].style.display = 'none';
                }}
            }}
        }}
    </script>

</body>
</html>
"""

# Convert the DataFrames to HTML

# Replace placeholders with actual tables
#html_content = html_template.format(table1=table1, table2=table2, table3=table3)

# Write the HTML to a file
with open('dataframes_with_search.html', 'w') as f:
    f.write(html_template)

print("HTML file with DataFrames generated successfully!")
