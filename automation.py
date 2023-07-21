from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def classTimeTable(request):
    import random
    json = {
            "no_of_days": 5,
            "period": 5,
            "school_time": "09:00 - 16:00",
            "lunch_time": "30 mins",
            "break_time": "10 mins",
            "lecture_time": "45 mins",
            "subjects": ["tamil", "english", "maths", "science", "social","science"],
            "class": "1-12",
            "teacher": ["tamil-priya", "english-sathiya", "maths-arun", "science-john", "social-hema"],
            "section": ["A","B","C"]
        }
    def generate_unique_table():
        table = []
        for i in range(len(json['teacher'])):
            row = json['teacher'].copy()
            if json['period'] >= len(row):
                row *= -(-json['period'] // len(row))
            random.shuffle(row)
            table.append(row)
        return table
    def has_same_value_at_same_index(table1, table2):
        for i in range(len(table1)):
            for j in range(len(table1[0])):
                if table1[i][j] == table2[i][j]:
                    return True
        return False

    num_tables = len(json["section"])
    tables = []

    for _ in range(num_tables):
        new_table = generate_unique_table()
        while any(has_same_value_at_same_index(new_table, t) for t in tables):
            new_table = generate_unique_table()
        tables.append(new_table)

    arr = []
    for table_idx, table in enumerate(tables, 1):
        arr.append(f"Table {table_idx}:")
        for row in table:
            arr.append(row)
        arr.append([])

    result_df = pd.DataFrame(arr)
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    result_df.to_excel(writer, index=False, index_label=False)
    writer._save()
    output.seek(0)
    # result_df.to_excel("Table1.xlsx", index=False, index_label=False)
    return HttpResponse(output, content_type='application/octet-stream')
