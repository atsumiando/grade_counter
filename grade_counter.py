def grade(score,total):
	if score >= total*0.9:
		letter = 'A'
	elif score >= total*0.8:
		letter = 'B'
	elif score >= total*0.7:
		letter = 'C'
	elif score >= total*0.6:
		letter = 'D'
	else:
		letter = 'F'
	return letter 


def finalgrade():
	import numpy as np
	with open('grades.txt', 'r') as sourcefile: #grade file is tab separate file called grades.txt
		list = sourcefile.read().splitlines()
		inputs, record = [], []
		for index in range(len(list)):
			record = list[index].split('\t')
			inputs.append(record)
	with open('finalgrade.txt' , 'w' ) as sinkfile: 
		start = int(input('Enter first quiz column: '))
		end = int(input('Enter last quiz column: '))
		start = int(start -2)
		end = int(end -2)
		for index in range(1,len(list)):
			data = inputs[index][1::]
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
			data = [float(x) for x in data]
			quiz = data[start:end]
			others = data[end::]
			quiz.remove(min(quiz))
			final = quiz + others
			sum = np.sum(final)
			score = float(sum)
			if inputs[index][0] == "Points":
				total = sum	
			sinkfile.write(inputs[index][0] +"\t"+str(sum)+"\t"+grade(score, total) +"\n")
	
		
finalgrade()

