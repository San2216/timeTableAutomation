import pandas as pd
from docx import Document
# import docx2txt
from pearl_core.settings import BASE_DIR


def extract_table_from_word(word_file):
    global typeNew
    typeNew = 0 #declare for checking the type of the table like multiple_choice or true_false
    try:
        #To check document extension for validation
        if word_file.split('.')[1] == "docx":
            # images = docx2txt.process(word_file, img_dir=BASE_DIR)
            doc = Document(word_file)
            table = doc.tables #get all pages as buffer

            # Initialize an empty list to store the table data
            data = []
            json_data = {}
            count = 0 #condition for checking wether its touch the first loop of first index 
            #Loop each pages
            for x in table:
                for row in x.rows: #taking document as each row.
                    row_data = [cell.text.strip() for cell in row.cells] #list comprehension method for appending entire row.
                    #Formating docx to excel cells
                    if row_data[0].startswith('Question'):
                        if count == 0:
                            json_data['Questions'] = row_data[1]
                            count += 1
                        else:
                            data.append(json_data.copy())
                            json_data.clear()
                            json_data['Questions'] = row_data[1]
                    if row_data[0] == 'Type':
                        if row_data[1] == 'multiple_choice':
                            typeNew = 1
                        if row_data[1] == 'integer':
                            typeNew = 2
                        if row_data[1] == 'fill_ups':
                            typeNew = 3
                        if row_data[1] == 'true_false':
                            typeNew = 4
                    if typeNew == 1:
                        if row_data[0] == 'Option':
                            if 'Option 1' not in json_data.keys(): #Check whether dict have this key.
                                json_data['Option 1'] = row_data[1]
                            elif 'Option 2' not in json_data.keys():
                                json_data['Option 2'] = row_data[1]
                            elif 'Option 3' not in json_data.keys():
                                json_data['Option 3'] = row_data[1]
                            elif 'Option 4' not in json_data.keys():
                                json_data['Option 4'] = row_data[1]
                        if row_data[0] == 'Solution':
                            json_data['Solution'] = row_data[1]
                        if row_data[0] == 'Marks':
                            json_data['Marks'] = row_data[2]
                    elif typeNew == 2:
                        if row_data[0] == 'Answer':
                            json_data['Answer'] = row_data[1]
                        if row_data[0] == 'Solution':
                            json_data['Solution'] = row_data[1]
                        if row_data[0] == 'Marks':
                            json_data['Marks'] = row_data[2]
                    elif typeNew == 3:
                        if row_data[0] == 'Option':
                            if 'Option 1' not in json_data.keys():
                                json_data['Option 1'] = row_data[1]
                            elif 'Option 2' not in json_data.keys():
                                json_data['Option 2'] = row_data[1]
                        if row_data[0] == 'Solution':
                            json_data['Solution'] = row_data[1]
                        if row_data[0] == 'Marks':
                            json_data['Marks'] = row_data[2]
                    elif typeNew == 4:
                        if row_data[0] == 'Answer':
                            json_data['Answer'] = row_data[1]
                        if row_data[0] == 'Solution':
                            json_data['Solution'] = row_data[1]
                        if row_data[0] == 'Marks':
                            json_data['Marks'] = row_data[2]
                    # data.append(row_data)

            return data
        else:
            return print("Upload Correct File")
    except Exception as e:
        print(str(e))
