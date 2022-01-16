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



class Predict:
    def __init__(self,news) -> None:
        self.news=news
    def predict(self):
        return manualTest(self.news).manual_test()




