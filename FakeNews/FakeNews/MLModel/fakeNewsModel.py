from nltk import text
import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from .Filters.allFilters import allFilters
from sklearn.metrics import accuracy_score
from sklearn.linear_model import PassiveAggressiveClassifier
nltk.download('punkt')

#load the dataset to train the model...its a csv file
df=pd.read_csv('F:\Class Work\Django\FakeNews\FakeNews\MLModel\Dataset\Train.csv')
#dropping null values from the data
df= df.dropna()  

#splitting the input and output parameters
x_df = df['text']
y_df = df['label']

#determing the training and the testing dataset size, for this model 25% is the test size 
x_train, x_test, y_train, y_test = train_test_split(x_df,y_df,test_size=0.25)

#Vectorize our data and fiting it
vectorization = TfidfVectorizer()
x_train = vectorization.fit_transform(x_train)
x_test = vectorization.transform(x_test)
pac=PassiveAggressiveClassifier(max_iter=50)
pac.fit(x_train,y_train)


def passiveAgressive(x_train,y_train,x_test,y_test):
    # filename = 'finalized_model.pkl'
    # joblib.dump(pac, filename)
    #Predict on the test set and calculate accuracy
    y_pred=pac.predict(x_test)
    score=accuracy_score(y_test,y_pred)
    return score


class manualTest:
    def __init__(self,news) -> None:
        self.news= news
    def wordopt(self,text):
        text= allFilters(text).filter() 
        return text
    def output_lable(self,n):
        if n == 0:
            return "Fake News"
        elif n == 1:
            return "Not A Fake News"

    def manual_test(self):
        testing_news = {"text":[self.news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(self.wordopt) 
        new_x_test = new_def_test["text"]
        new_xv_test = vectorization.transform(new_x_test)
        # filename = 'finalized_model.pkl'
        # loaded_model = joblib.load(open(filename, 'rb'))

        pred_pac = pac.predict(new_xv_test)

        print(pred_pac)

        # return print("\nPassiveAggressiveClassifier Prediction: {}".format(self.output_lable(pred_pac[0])))
        return self.output_lable(pred_pac[0])

news='''House Dem Aide: We Didn’t Even See Comey’s Letter Until Jason Chaffetz Tweeted It,Darrell Lucus,"House Dem Aide: We Didn’t Even See Comey’s Letter Until Jason Chaffetz Tweeted It By Darrell Lucus on October 30, 2016 Subscribe Jason Chaffetz on the stump in American Fork, Utah ( image courtesy Michael Jolley, available under a Creative Commons-BY license) 
With apologies to Keith Olbermann, there is no doubt who the Worst Person in The World is this week–FBI Director James Comey. But according to a House Democratic aide, it looks like we also know who the second-worst person is as well. It turns out that when Comey sent his now-infamous letter announcing that the FBI was looking into emails that may be related to Hillary Clinton’s email server, the ranking Democrats on the relevant committees didn’t hear about it from Comey. They found out via a tweet from one of the Republican committee chairmen. 
As we now know, Comey notified the Republican chairmen and Democratic ranking members of the House Intelligence, Judiciary, and Oversight committees that his agency was reviewing emails it had recently discovered in order to see if they contained classified information. Not long after this letter went out, Oversight Committee Chairman Jason Chaffetz set the political world ablaze with this tweet. FBI Dir just informed me, ""The FBI has learned of the existence of emails that appear to be pertinent to the investigation."" Case reopened 
— Jason Chaffetz (@jasoninthehouse) October 28, 2016 
Of course, we now know that this was not the case . Comey was actually saying that it was reviewing the emails in light of “an unrelated case”–which we now know to be Anthony Weiner’s sexting with a teenager. But apparently such little things as facts didn’t matter to Chaffetz. The Utah Republican had already vowed to initiate a raft of investigations if Hillary wins–at least two years’ worth, and possibly an entire term’s worth of them. Apparently Chaffetz thought the FBI was already doing his work for him–resulting in a tweet that briefly roiled the nation before cooler heads realized it was a dud. 
But according to a senior House Democratic aide, misreading that letter may have been the least of Chaffetz’ sins. That aide told Shareblue that his boss and other Democrats didn’t even know about Comey’s letter at the time–and only found out when they checked Twitter. “Democratic Ranking Members on the relevant committees didn’t receive Comey’s letter until after the Republican Chairmen. In fact, the Democratic Ranking Members didn’ receive it until after the Chairman of the Oversight and Government Reform Committee, Jason Chaffetz, tweeted it out and made it public.” 
So let’s see if we’ve got this right. The FBI director tells Chaffetz and other GOP committee chairmen about a major development in a potentially politically explosive investigation, and neither Chaffetz nor his other colleagues had the courtesy to let their Democratic counterparts know about it. Instead, according to this aide, he made them find out about it on Twitter. 
There has already been talk on Daily Kos that Comey himself provided advance notice of this letter to Chaffetz and other Republicans, giving them time to turn on the spin machine. That may make for good theater, but there is nothing so far that even suggests this is the case. After all, there is nothing so far that suggests that Comey was anything other than grossly incompetent and tone-deaf. 
What it does suggest, however, is that Chaffetz is acting in a way that makes Dan Burton and Darrell Issa look like models of responsibility and bipartisanship. He didn’t even have the decency to notify ranking member Elijah Cummings about something this explosive. If that doesn’t trample on basic standards of fairness, I don’t know what does. 
Granted, it’s not likely that Chaffetz will have to answer for this. He sits in a ridiculously Republican district anchored in Provo and Orem; it has a Cook Partisan Voting Index of R+25, and gave Mitt Romney a punishing 78 percent of the vote in 2012. Moreover, the Republican House leadership has given its full support to Chaffetz’ planned fishing expedition. But that doesn’t mean we can’t turn the hot lights on him. After all, he is a textbook example of what the House has become under Republican control. And he is also the Second Worst Person in the World. About Darrell Lucus 
Darrell is a 30-something graduate of the University of North Carolina who considers himself a journalist of the old '''
# accuracy=passiveAgressive(x_train,y_train,x_test,y_test)
# print(f'Accuracy: {round(accuracy*100,2)}%')
# manualTest(news).manual_test()

class Predict:
    def __init__(self,news) -> None:
        self.news=news
    def predict(self):
        return manualTest(self.news).manual_test()




