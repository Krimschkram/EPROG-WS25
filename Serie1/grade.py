final_exam = 100
weekly_exam = 100
excercis = 100

grade_num = (0.4 * final_exam + 0.4 * weekly_exam + 0.2* excercis)
grade_string = "Nicht Genügend"

if grade_num > 50:
    grade_string = "Genügend"
if grade_num > 62.5:
    grade_string = "Befriedigend"
if grade_num > 75:
    grade_string = "Gut"
if grade_num > 87.5:
    grade_string = "Sehr gut"

print("Deine finale Note ist:",grade_string)


