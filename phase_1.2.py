from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re,string,json,datetime
#flnm = "twitter_user_data_%i.%i.%i.txt" % (datetime.datetime.now().month, datetime.datetime.now().day, datetime.datetime.now().year)
flnm="twitter_user_data_3.5.2017.txt"
def proc_tweet(text):
    text=re.sub(r'([A-Z]\.)+',"",text) #abbrevation
    text=re.sub(r'(@\w+:* )+',"",text) #mentions in tweets
    text=re.sub(r'\$?\d+(\.\d+)?%?',"",text) #currency
    text=re.sub(r'\w+[\x90-\xff]',"",text) #emoji
    text=re.sub(r'https:\/\/\w.\w\w\/\w+',"",text) #twitter urls
    text=re.sub(r'(\.)+',"",text) #multiple full stops
    text=re.sub(r'(\\u\d+\w+)+',"",text) #utf-16 stuff
    stop =  stop= stopwords.words('english') + list(string.punctuation)+ ['rt',"'"]
    text=" ".join([i for i in word_tokenize(text.lower()) if i not in stop])
    return text
try:
    with open(flnm,'r') as readfile:
        text_data = readfile.read()
except:
    print "file error"
finally:
    #print 1
    readfile.close()
json_data=json.loads(text_data)
ls=[]
k=0
for i in json_data:
    k+=1
    a={}
    for key in i:
        a.update({key:i[key]})
    a.update({'Processed: ': proc_tweet(a['text'])})
    print a['Processed: ']
    s=raw_input("Enter Positive or Negative sentiment for this Text(0/1): ")
    a.update({"Sentiment: ": s})
    ls.append(a)
    if k>21:
        break
try:
    with open("1.txt",'w') as outfile:
        json_obj=json.dump(ls,outfile,sort_keys='True',indent=4)
except:
    print "file error"
finally:
    outfile.close()
