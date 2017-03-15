import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

flnm = "1.txt"
try:
    with open(flnm,'r') as readfile:
        text_data = readfile.read()
except:
        text_data = readfile.read()
        print "file error"
finally:
    readfile.close()
json_data=json.loads(text_data)
t_d=[]
t_l=[]
for i in json_data:
    t_d.append(i['Processed: '])
    t_l.append(i['Sentiment: '])

vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(t_d)

    # Perform classification with SVM, kernel=rbf
classifier_rbf = svm.SVC()
#t0 = time.time()
classifier_rbf.fit(train_vectors, t_l)
#t1 = time.time()
#prediction_rbf = classifier_rbf.predict(test_vectors)
#t2 = time.time()
#time_rbf_train = t1-t0
#time_rbf_predict = t2-t1
a=["democrats inquirey into sessions "]
print classifier_rbf.predict(vectorizer.fit_transform(a))
