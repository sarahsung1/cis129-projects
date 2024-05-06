#Lab 11 Exercises 9.1, 9.2, 9.3
#Sarah Sung
#May 6, 2024
#Writes grades to text file

#9.1
def write_grades_txt_file():
    with open('grades.txt', 'w') as file:
        print("""Please enter grades (enter "end" to end the entry process)""")
        while True:
            grade = input("Enter a grade: ")
            if grade.lower() == "end":
                break
            file.write(grade + "\n")

#9.2
def read_grades_txt_file():
    with open('grades.txt', 'r') as file:
        grades_list = []
        for grade_line in file.readlines():
            try:
                add_grade = int(grade_line.strip())
                grades_list.append(add_grade)
            except ValueError:
                print(f"Invalid grade, '{grade_line.strip()}' omitted")
#calculate total
total = sum(grades_list)
count = len(grades_list)
average = total/count if count > 0 else 0
#display individual grades
print("Individual grades:", grades_list)
print("Total sum of grades:", total)
print("Number of grades:", count)
print("Grade average:", average)

#9.3
def write_student_record_csv():
    import csv
    with open('grades.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        while True:
            firstname = input("""Enter the student's first name (enter "end" to end the entry process):""")
            if firstname.lower() == "end":
                break
            lastname = input("Enter the student's last name: ")
            exam1grade = input("Enter the grade for exam 1: ")
            exam2grade = input("Enter the grade for exam 2: ")
            exam3grade = input("Enter the grade for exam 3: ")
            writer.writerow([firstname,lastname,exam1grade,exam2grade,exam3grade])
#call each function
write_grades_txt_file()
read_grades_txt_file()
write_student_record_csv()