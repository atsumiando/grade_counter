# grade_counter
Calculate total scores and grades for each students with a function of removing minimum score of quizzes. 

It is python codes and use "python grade_counter.py" to run!
# File format 

	Name	ID	quiz1	quiz2	quiz3	quiz4	exam1	exam2	journal_club	attendance	assignment	
	Points	total	10	10	10	10	100	100	20	20	20	
	NAME1	id1	5	6	7	8	99	80	20	20	10	
	NAME2	id2	5	7	7	9	96	78	12	17	5	

# Description of file format
Quizzes should locate first part of scores. 
Codes ask you total maximum scores, start position of quiz row and score column, input and output file names. 
At the end, codes ask you whether you need to remove minimum scores of quizzes or not. 
If your answer is yes, codes ask you to type first and last collumn of quizzes. 

Questions are followings (with example answers) ...

What is maximum scores?: 500
Which row does grading start: 3
Which column does scores start: 3
Input file name is (add quotation marks): 'grades.txt'
Output file name is (add quotation marks): 'finalgrades.txt'
Do you need to remove minimum scores of quizzes? (add quotation marks) : 'yes'
Enter first quiz column: 3
Enter last quiz column: 8
# Outcome

	NAME1	id1 250	B #from 2nd_line(students total scores and grade)
	NAME2	id2 231	C #from 2nd_line(students total scores and grade)

It is set A>=92%, 92%>A->88%, 88%>B+>=84%, 84%>B>=80%, 80%>B->=76%, 76%>C+>=72%, 72%>C>=68%, 68%>C->=64%, 64%>D+>=60, 60%>D>=56%, 56%>D->=52%, and F<52%.
