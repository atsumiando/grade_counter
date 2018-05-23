# grade_counter
Calculate total scores and grades for each students with a function of removing minimum score of quizzes. 

It is python codes and use grade_counter.py to run!
# File format 

		quiz1	quiz2	quiz3	quiz4	exam1	exam2	journal_club	attendance	assignment	#1st_line(header)
	Points	10	10	10	10	100	100	20	20	20	#2nd_line(Points)
	NAME1	5	6	7	8	99	80	20	20	10	#from 3rd_line(students scores)
	NAME2	5	7	7	9	96	78	12	17	5	#from 3rd_line(students scores)


# Description of file format
File name is "grades.txt" and format is tab split file. Example "grades.txt" had been uploaded.

First line is header of contents(e.g. quiz, exam, attendance, etc...)

Second line is points of each content ( e.g. quiz, exam, attendance, etc...) and first column name is "Points". 

First collumn is name of students from thired lines.

Blank is allowed in each contents. 

Column of quizzes need to be located continuously (quizzes: 2nd-7th column) not random (quizzes:2-4th and 7-10th column).

# Outcome
Outcome is "finalgrade.txt".

	Points	290	A #1st_line(Points, total scores and maximum grade)
	NAME1	250	B #from 2nd_line(students total scores and grade)
	NAME2	231	C #from 2nd_line(students total scores and grade)

It is set A>=90%, 90%>B>=80%,  80%>C>=70%, 70%>D>=60%, and F<60%.

First line is "Points", which are total scores and maximum grade. 

After scond lines, first column is name of students, second column is total scores of each students, and last column is grade of each students. 

