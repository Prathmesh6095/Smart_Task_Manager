import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = {
"task":[
"submit project today",
"prepare exam tomorrow",
"finish assignment tonight",
"meeting with manager",
"client presentation",
"buy groceries",
"watch movie",
"go to gym"
],

"priority":[
"High",
"High",
"High",
"Medium",
"High",
"Low",
"Low",
"Medium"
]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["task"])

model = MultinomialNB()
model.fit(X, df["priority"])

joblib.dump(model,"priority_model.pkl")
joblib.dump(vectorizer,"vectorizer.pkl")

print("AI model trained successfully")