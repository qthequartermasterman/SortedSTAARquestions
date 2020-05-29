import csv
from collections import defaultdict
import glob
from tempfile import NamedTemporaryFile
import shutil

list_of_staar_expectations = glob.glob('staar_exam_keys/*.csv')
# List of filepaths to CSV files of STAAR expectations tested on a given exam. These are downloaded from:
# https://tea.texas.gov/student-assessment/testing/staar/staar-student-expectations-tested
# The list of URLS is also in "filenames.txt"

questions = []

questions_by_content_teks = defaultdict(list)
questions_by_process_teks = defaultdict(list)


# Extract all the question data
for doc in list_of_staar_expectations:
    if 'math' in doc or 'Math' in doc or 'Algebra' in doc:
        # Math documents format their process TEKS pretty strangely
        # Instead of listing them in each row's cell, each process TEKS gets its own column
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(doc, 'r') as csvfile, tempfile:
            reader = csv.reader(csvfile)
            writer = csv.writer(tempfile)
            header1 = next(reader)
            if 'PROCESS STUDENT EXPECTATIONS' in header1:
                header2 = next(reader)
                if header2[0] is '':
                    for h in range(len(header2)):
                        if header2[h] is not '':
                            header1[h] = header2[h]
                    writer.writerow(header1)
                    while True:
                        try:
                            writer.writerow(next(reader))
                        except StopIteration:
                            break
                    shutil.move(tempfile.name, doc)
    with open(doc) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                questions.append(row)

# Organize by TEKS
for q in questions:
    if 'SUBJECT' in q.keys():
        if 'CONTENT STUDENT EXPECTATION' in q.keys():
            questions_by_content_teks[q['SUBJECT'] +' '+ q['CONTENT STUDENT EXPECTATION']].append(q)
        if 'PROCESS STUDENT EXPECTATION' in q.keys():
            questions_by_process_teks[q['SUBJECT'] +' '+ q['PROCESS STUDENT EXPECTATION']].append(q)
        if q['SUBJECT'] in ['Mathematics', 'Algebra I']:
            # Because Math questions' process teks are formatted funny, we have to extract each one individually.
            for key in q.keys():
                if '.' in key:  # If there is a period in the key, it must be a TEKS statement
                    if q[key] is not '':  # There is some marking indicating the question tests that TEKS
                        questions_by_process_teks[q['SUBJECT'] +' '+key].append(q)

with open('STAAR_QUESTIONS_LIST_CONTENT.csv', 'w+') as file:
    writer = csv.writer(file)
    for teks in iter(sorted(questions_by_content_teks.items())):
        row = [f'{teks[0]}']
        # print(f'{teks[0]}:', end='\t\t')
        for q in teks[1]:
            row.append(f'{q["TEST DATE"]} {q["LANGUAGE"] if "LANGUAGE" in q.keys() else None} #{q["ITEM"]}')
            # print(f'{q["TEST DATE"]} #{q["ITEM"]}', end='\t\t')
        writer.writerow(row)
        print(row)

with open('STAAR_QUESTIONS_LIST_PROCESS.csv', 'w+') as file:
    writer = csv.writer(file)
    for teks in iter(sorted(questions_by_process_teks.items())):
        row = [f'{teks[0]}']
        # print(f'{teks[0]}:', end='\t\t')
        for q in teks[1]:
            row.append(f'{q["TEST DATE"]} {q["LANGUAGE"] if "LANGUAGE" in q.keys() else None} #{q["ITEM"]}')
            # print(f'{q["TEST DATE"]} #{q["ITEM"]}', end='\t\t')
        writer.writerow(row)
        print(row)


