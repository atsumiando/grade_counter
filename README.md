# grade_counter
Calculate total scores and grades for each students.

This code have function to remove minimum score of quizzes. 

# File format 

		quiz1	quiz2	quiz3	quiz4	exam1	exam2	journal_club	attendance	assignment	#1st_line(header)
	Points	10	10	10	10	100	100	20	20	20	#2nd_line(Points)
	NAME	5	6	7	8	99	80	20	20	10	#from 3rd_line(students scores)


# Description of file format
First line is header of contents(e.g. quiz, exam, attendance, etc...)

Second line is points of each content ( e.g. quiz, exam, attendance, etc...) and first column name is "Points". 

First collumn is name of students from thired lines.

Blank is allowed in each contents. 

Column of quizzes need to be located continuously (quizzes: 2nd-7th column) not random (quizzes:2-4th and 7-10th column).
