from sklearn.feature_extraction.text import TfidfTransformer
import csv
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
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
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(di)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print X_train_tfidf.shape
clf = MultinomialNB().fit(X_train_tfidf,cl)

dit=['13','5','2','7','4','12']
X_new_counts = count_vect.transform(dit)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
predicted = clf.predict(X_new_tfidf)
print predicted
