import random
from itertools import permutations
import pandas as pd

def TestFunc(teacher_count):
    # Define the sections, periods, and days
    sections = ['Section A', 'Section B', 'Section C', 'Section D', 'Section E']
    periods = ["tamil-priya", "english-sathiya", "maths-arun", "science-john", "social-hema"]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Function to check if the timetable has no duplicate subjects on the same period and day
    def is_valid_timetable(timetable):
        for day, period in enumerate(timetable):
            if timetable.count(period) > 1:
                return False
        return True

    # Generate all possible permutations of periods for each day
    possible_timetables = permutations(periods, len(days))

    # Create an empty list to store valid timetables
    valid_timetables = []

    # Iterate through each timetable and check the uniqueness conditions
    for timetable in possible_timetables:
        if is_valid_timetable(timetable):
            valid_timetables.append(timetable)

    # If teacher_count is less than the total number of periods, ensure that each period is assigned to a teacher at least once
    if teacher_count < len(periods):
        required_periods = set(random.sample(periods, teacher_count))
        valid_timetables = [timetable for timetable in valid_timetables if set(timetable).issuperset(required_periods)]

    # Create a DataFrame to store the timetable data
    timetable_df = pd.DataFrame(columns=['Day'] + sections)

    # Iterate through each valid timetable and populate the DataFrame
    for v in sections:
        for day, timetable in zip(days, valid_timetables):
            shuffled_timetable = random.sample(timetable, len(timetable))
            timetable_data = [day] + shuffled_timetable
            timetable_df = timetable_df._append(pd.Series(timetable_data, index=timetable_df.columns), ignore_index=True)

    # Set the Day column as the index for better visualization
    # timetable_df.set_index('Day', inplace=True)

    timetable_df.to_excel("Table2.xlsx", index=False, index_label=False)

# Set the number of teachers available (change this value accordingly)
teacher_count = 5

TestFunc(teacher_count)




# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def classTimeTable(request):
#     import random
#     json = {
#             "no_of_days": 5,
#             "period": 5,
#             "school_time": "09:00 - 16:00",
#             "lunch_time": "30 mins",
#             "break_time": "10 mins",
#             "lecture_time": "45 mins",
#             "subjects": ["tamil", "english", "maths", "science", "social","science"],
#             "class": "1-12",
#             "teacher": ["tamil-priya", "english-sathiya", "maths-arun", "science-john", "social-hema"],
#             "section": ["A","B","C"]
#         }
#     def generate_unique_table():
#         table = []
#         for i in range(len(json['teacher'])):
#             row = json['teacher'].copy()
#             if json['period'] >= len(row):
#                 row *= -(-json['period'] // len(row))
#             random.shuffle(row)
#             table.append(row)
#         return table
#     def has_same_value_at_same_index(table1, table2):
#         for i in range(len(table1)):
#             for j in range(len(table1[0])):
#                 if table1[i][j] == table2[i][j]:
#                     return True
#         return False

#     num_tables = len(json["section"])
#     tables = []

#     for _ in range(num_tables):
#         new_table = generate_unique_table()
#         while any(has_same_value_at_same_index(new_table, t) for t in tables):
#             new_table = generate_unique_table()
#         tables.append(new_table)

#     arr = []
#     for table_idx, table in enumerate(tables, 1):
#         arr.append(f"Table {table_idx}:")
#         for row in table:
#             arr.append(row)
#         arr.append([])

#     result_df = pd.DataFrame(arr)
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')
#     result_df.to_excel(writer, index=False, index_label=False)
#     writer._save()
#     output.seek(0)
#     # result_df.to_excel("Table1.xlsx", index=False, index_label=False)
#     return HttpResponse(output, content_type='application/octet-stream')
