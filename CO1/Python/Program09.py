import csv


total_marks = 0
subject1_sum = 0
subject2_sum = 0
subject3_sum = 0
highest_mark = -1
second_highest_mark = -1
highest_student = None
second_highest_student = None


with open('Rank.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    
    for row in csv_reader:
        
        rollno = int(row['rollno'])
        name = row['name']
        branch = row['branch']
        m1 = int(row['m1'])
        m2 = int(row['m2'])
        m3 = int(row['m3'])
        
        
        total_marks += m1 + m2 + m3
        
 
        subject1_sum += m1
        subject2_sum += m2
        subject3_sum += m3
        
   
        current_total = m1 + m2 + m3
        if current_total > highest_mark:
            second_highest_mark = highest_mark
            second_highest_student = highest_student
            highest_mark = current_total
            highest_student = (rollno, name)
        elif current_total > second_highest_mark:
            second_highest_mark = current_total
            second_highest_student = (rollno, name)


num_students = csv_reader.line_num - 1  
average_subject1 = subject1_sum / num_students
average_subject2 = subject2_sum / num_students
average_subject3 = subject3_sum / num_students


print("Total Marks of All Students:", total_marks)
print("Average Marks (Subject 1):", average_subject1)
print("Average Marks (Subject 2):", average_subject2)
print("Average Marks (Subject 3):", average_subject3)
print("Student with Highest Marks:", highest_student[1], "with Roll No.", highest_student[0])
print("Student with Second Highest Marks:", second_highest_student[1], "with Roll No.", second_highest_student[0])