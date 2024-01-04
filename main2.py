import json

with open('students.json') as file:
    students = json.load(file)
# print(students)
print(f"birinchi talabaning ismi {students['student'][0]['name']}, "
      f"familiyasi {students['student'][0]['lastname']}, " 
      f"{students['student'][0]['year']}-kurs talabasi, " 
      f"{students['student'][0]['faculty']} fakulteti talabasi \n"
      f"ikkinchi talabaning ismi {students['student'][1]['name']}, "
      f"familiyasi {students['student'][1]['lastname']}, " 
      f"{students['student'][1]['year']}-kurs talabasi, " 
      f"{students['student'][1]['faculty']} fakulteti talabasi \n"
      f"uchinchi talabaning ismi {students['student'][2]['name']}, "
      f"familiyasi {students['student'][2]['lastname']}, " 
      f"{students['student'][2]['year']}-kurs talabasi, " 
      f"{students['student'][2]['faculty']} fakulteti talabasi \n") 