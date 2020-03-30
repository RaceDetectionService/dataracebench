import csv

#file = open('tsan-clang.csv',"r")
#lines = file.readlines()
lines = csv.reader(open('f1.csv',"r"))
data = list(lines)
#content = [line.strip() for line in lines]
truth = []
races = []
truePositive = 0
falsePositive = 0
trueNegative = 0
falseNegative = 0
positive = 0
negative = 0
for item in data:
	truth.append(item[1])
	races.append(item[3])
for i in range(len(truth)):
	if truth[i] == 'TRUE':
		positive += 1 
		if races[i] == '0':
			falsePositive += 1
		else:
			truePositive += 1
	else:
		negative += 1 
		if races[i] == '0':
			trueNegative += 1
		else:
			falseNegative += 1
print("false positive is ", falsePositive)
print("true positive is ", truePositive)
print("true negative is ", trueNegative)
print("false negative is ", falseNegative)
Accuracy = (truePositive + trueNegative) / len(truth)
Precision = truePositive / (truePositive + falsePositive)
Recall = truePositive / (truePositive + falseNegative)
f1Score = 2 * Precision * Recall / (Precision + Recall)
print("Accuracy is ", Accuracy)
print("Precision ", Precision)
print("Recall is ", Recall)
print("F1 Score is ", f1Score)
