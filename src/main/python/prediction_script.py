# add_numbers.py
import sys
import numpy as np
import pandas as pd
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import joblib
import warnings

# Suppress UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

DATA_PATH = r"C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\Training.csv"
data = pd.read_csv(DATA_PATH).dropna(axis = 1)



encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:,:-1]
y = data.iloc[:, -1]



from statistics import mode

# Reading the test data
test_data = pd.read_csv(r"C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\Testing.csv").dropna(axis=1)

test_X = test_data.iloc[:, :-1]
test_Y = encoder.fit_transform(test_data.iloc[:, -1])



symptoms = X.columns.values

# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":encoder.classes_
}

def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1

    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1,-1)

    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]

    # making final prediction by taking mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction":final_prediction
    }
    return nb_prediction


# Example usage
if __name__ == "__main__":

    final_svm_model = joblib.load(r'C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\final_svm_model.joblib')
    final_nb_model = joblib.load(r'C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\final_nb_model.joblib')
    final_rf_model = joblib.load(r'C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\final_rf_model.joblib')
    encoder = joblib.load(r'C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\label_encoder.joblib')
    symptom_index = joblib.load(r'C:\Users\Saikat Moi\Downloads\JavaSpringBoot\predictionofdisease\src\main\resources\models\symptom_index.joblib')
    temp=sys.argv[1]
    result = predictDisease(temp)
    print(result)