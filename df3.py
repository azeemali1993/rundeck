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

# Convert the DataFrames to HTML
table1 = df1.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table1')
table2 = df2.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table2')
table3 = df3.to_html(index=False, classes='table table-striped table-bordered', border=0, table_id='table3')

# HTML template with collapsible tables using Bootstrap

# Write the HTML to a file
html_template = f'''
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
            text-align: center;
        }}
        table {{
            margin: 0 auto;
            width: auto; /* Table width adjusts according to the content */
            max-width: 100%;
        }}
        th, td {{
            text-align: left; /* Align table content to the left */
        }}
        .search-box {{
            margin-bottom: 15px;
        }}
        .collapse-btn {{
            margin-bottom: 15px;
        }}
    </style>
</head>
<body>

    <button class="btn btn-primary collapse-btn" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTable1" aria-expanded="true" aria-controls="collapseTable1">
        Summary
    </button>
    <div class="collapse show" id="">
        {table1}
    </div>

    
    <button class="btn btn-primary collapse-btn" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTable2" aria-expanded="true" aria-controls="collapseTable2">
        Audit Table
    </button>
    <div class="collapse" id="collapseTable2">
       <input class="form-control search-box" type="text" id="search2" onkeyup="searchTable(2)" placeholder="Search for anything...">
        {table2}
    </div>

    <button class="btn btn-primary collapse-btn" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTable3" aria-expanded="true" aria-controls="collapseTable3">
        Process Log
    </button>
    <div class="collapse" id="collapseTable3">
    <input class="form-control search-box" type="text" id="search3" onkeyup="searchTable(3)" placeholder="Search for anything...">
        {table3}
    </div>

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
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''
with open('dataframes_with_search.html', 'w') as f:
    f.write(html_template)

print("HTML file with collapsible DataFrames generated successfully!")
