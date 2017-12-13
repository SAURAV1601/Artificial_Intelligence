#This program using 1024 features given in the dataset to train the neural network and predict the given digit
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
# Intializing x and y vetcors for training neural network
# x vector has 1024 features of the digits and y has the value of feature corresponding in x vector
digits=[]
values=[]
i=0
digits.append([])
# ignoring all data till the line lastparag is reached
while 1:
	row=raw_input()
	if row=='lastparag = 0':
		break
# Reading the file line by line
while 1:
	row=raw_input()
	if row=="EOF":
		break
	else:	
		#constructing the feature vector
		if i<32:
			for c in list(row):
				digits[-1].append(int(c))
			i+=1
		#constructing value vector
		if i==32:
			number=raw_input()
			values.append(number.strip(' \t\n\r'))
			i=0
			digits.append([])
digits.pop()

# Building classifier
# hidden nodes is given as 500 and can be changes to any value like 10,100,1000,so on
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(500))
#Spliting the given data in training and testing data (training is 80% and testing is 20%)
X_train, X_test, y_train, y_test = train_test_split(digits, values, test_size=0.2)
# Creating the model
model = clf.fit(X_train, y_train)
# Predicting values for test data
predictions = clf.predict(X_test)

#Printing the classification report 
target_names = ['0','1','2','3','4','5','6','7','8','9']
print classification_report(y_test, predictions, target_names=target_names)

