total = int(input('what is maximum scores?: '))
header = int(input('Which row does grading start: '))
grading_scores = int(input('Which column does scores start: '))
input_file_name = str(input('Input file name is (add quotation marks): '))
output_file_name = str(input('Output file name is (add quotation marks): '))

def grade(score):#define grades
	if score >= 0.92*total:
		letter = 'A'
	elif score >= 0.88*total:
		letter = 'A-'
	elif score >= 0.84*total:
		letter = 'B+'
	elif score >= 0.80*total:
		letter = 'B'
	elif score >= 0.76*total:
		letter = 'B-'
	elif score >= 0.72*total:
		letter = 'C+'
	elif score >= 0.68*total:
		letter = 'C'
	elif score >= 0.64*total:
		letter = 'C-'
	elif score >= 0.60*total:
		letter = 'D+'
	elif score >= 0.56*total:
		letter = 'D'
	elif score >= 0.52*total:
		letter = 'D-'
	else:
		letter = 'F'
	return letter 

def filename():
	with open(input_file_name, 'r') as sourcefile:#add your file name and separate data in lines
		list = sourcefile.read().splitlines()
		inputs, record = [], []
		for index in range(len(list)):
			record = list[index].split('\t')
			inputs.append(record)
	with open('exchange_to_numerical_data' , 'w' ) as sinkfile: #make new file
		for index in range(header-1,len(list)): #run lines from second to last (first = header)
			data = inputs[index][grading_scores-1::]
			data = [x.replace('', 'a') for x in data]
			data = [x.replace('a1', '1') for x in data]
			data = [x.replace('a2', '2') for x in data]
			data = [x.replace('a3', '3') for x in data]
			data = [x.replace('a4', '4') for x in data]
			data = [x.replace('a5', '5') for x in data]
			data = [x.replace('a6', '6') for x in data]
			data = [x.replace('a7', '7') for x in data]
			data = [x.replace('a8', '8') for x in data]
			data = [x.replace('a9', '9') for x in data]
			data = [x.replace('a0', '0') for x in data]
			data = [x.replace('1a', '1') for x in data]
			data = [x.replace('2a', '2') for x in data]
			data = [x.replace('3a', '3') for x in data]
			data = [x.replace('4a', '4') for x in data]
			data = [x.replace('5a', '5') for x in data]
			data = [x.replace('6a', '6') for x in data]
			data = [x.replace('7a', '7') for x in data]
			data = [x.replace('8a', '8') for x in data]
			data = [x.replace('9a', '9') for x in data]
			data = [x.replace('0a', '0') for x in data]
			data = [x.replace('a', '0') for x in data]
			data = [float(x) for x in data]#replace '' to '0'
			number ='\t'.join(str(e) for e in data)
			id = inputs[index][:grading_scores-1]
			id_str= [str(x) for x in id]
           		ID ='\t'.join(str(e) for e in id_str)
			sinkfile.write(ID +"\t"+number+"\n")

def finalgrade_rm_min():
	import numpy as np
	start = int(input('Enter first quiz column: '))
	end = int(input('Enter last quiz column: '))
	with open('exchange_to_numerical_data', 'r') as sourcefile:#add your file name and separate data in lines
		list = sourcefile.read().splitlines()
		inputs, record = [], []
		for index in range(len(list)):
			record = list[index].split('\t')
			inputs.append(record)
	with open(output_file_name, 'w' ) as sinkfile: #make new file
		for index in range(len(list)):
			data = inputs[index][int(grading_scores)-1::]
			data = [float(x) for x in data]
			starts = int(start -int(grading_scores))
			ends = int(end -int(grading_scores)+1)
			quiz = data[starts:ends]#identify quiz collumns
			others = data[ends::]#identify other scores
			quiz.remove(min(quiz))#remove minimum quiz score
			final = quiz + others#add all scores
			sum = np.sum(final)#sum all scores 
			score = float(sum)
			id = inputs[index][:grading_scores-1]
			id_str= [str(x) for x in id]
           		ID ='\t'.join(str(e) for e in id_str)
			sinkfile.write(ID +"\t"+str(sum)+"\t"+grade(score) +"\n")
	
def finalgrade():
	import numpy as np
	with open('exchange_to_numerical_data', 'r') as sourcefile:#add your file name and separate data in lines
		list = sourcefile.read().splitlines()
		inputs, record = [], []
		for index in range(len(list)):
			record = list[index].split('\t')
			inputs.append(record)
	with open(output_file_name, 'w' ) as sinkfile: #make new file
		for index in range(len(list)):
			data = inputs[index][int(grading_scores)-1::]
			final = [float(x) for x in data]
			sum = np.sum(final)#sum all scores 
			score = float(sum)
			id = inputs[index][:grading_scores-1]
			id_str= [str(x) for x in id]
           		ID ='\t'.join(str(e) for e in id_str)
			sinkfile.write(ID +"\t"+str(sum)+"\t"+grade(score) +"\n")

def yes_or_no():
	x = str(input('Do you need to remove minimum scores of quizzes? (add quotation marks) : '))
	if x == 'no':
		return finalgrade()
	if x == 'yes':
		return finalgrade_rm_min()


filename()
yes_or_no()





