
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
import csv
fn="DataSet_2D_LinearlySeparable.csv"
cl=[]
di=[]
try:
    with open(fn,'rb') as fl:
        reader = csv.reader(fl)
        for row in reader:
            cl.append(row[2])
            di.append(row[3])
            
except:
    print 1
finally:
    fl.close()
#print cl,di
vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(di)
classifier_rbf = svm.SVC()
classifier_rbf.fit(train_vectors, cl)
dit=['13','5','2','7','4','12']
prediction_rbf = classifier_rbf.predict(vectorizer.transform(dit))
print prediction_rbf

''' text data

flnm = "amazon_cells_labelled_train.txt"
try:
    with open(flnm,'r') as readfile:
        text_data = readfile.readlines()
except:
        text_data = readfile.read()
        print "file error"
finally:
    readfile.close()
t_d=[]
t_l=[]
for line in text_data:
    words = line.split('\t')
    t_d.append(words[0])
    t_l.append(words[1])

vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(t_d)

    # Perform classification with SVM, kernel=rbf
classifier_rbf = svm.SVC()
classifier_rbf.fit(train_vectors, t_l)
#prediction_rbf = classifier_rbf.predict(test_vectors)

flnm = "amazon_cells_labelled_test.txt"
try:
    with open(flnm,'r') as readfile:
        text_data = readfile.readlines()
except:
        text_data = readfile.read()
        print "file error"
finally:
    readfile.close()
t_d1=[]
t_l1=[]
for line in text_data:
    words = line.split('\t')
    t_d1.append(words[0])
    t_l1.append(words[1])

test_vectors = vectorizer.transform(t_d1)
prediction_rbf = classifier_rbf.predict(test_vectors)
e=0
for u in range(0,len(prediction_rbf)):
    #print t_l1[u],prediction_rbf[u]
    if prediction_rbf[u]!=t_l1[u]:
        e=e+1 
print prediction_rbf
print t_l1
print e
'''