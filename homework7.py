grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list_1 = sorted(students)
list(grades)
a = grades[0]
Aaron_ball = sum(a) / len(a)
b = grades[1]
Bilbo_ball = sum(b) / len(b)
c = grades[2]
Johnny_ball = sum(c) / len(c)
d = grades[3]
Khendrik_ball = sum(d) / len(d)
e = grades[4]
Steve_ball = sum(e) / len(e)
average_score = {students_list_1[0]: Aaron_ball, students_list_1[1]:Bilbo_ball, students_list_1[2]: Johnny_ball, students_list_1[3]: Khendrik_ball, students_list_1[4]:Steve_ball}
print(average_score)