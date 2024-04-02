from tokenize import Double
from flask import Flask,request, jsonify, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
    print(prediction)
    output='{0:.{1}f}'.format(prediction[0], 2)


    if float(output)<3: 
        return render_template("index.html", pred="The maximum magnitude of an earthquake possible at this location is: "+output+"\nThe earthquake is tolerable. It will only have small virations. \nRISK is LOW!")
    elif float(output)>6:
        return render_template("index.html", pred="The maximum magnitude of an earthquake possible at this location is: "+output+"\nThe earthquake is very sever. High risk of loss of life and property. \nRISK is VERY HIGH!")
    else:
        return render_template("index.html", pred="The maximum magnitude of an earthquake possible at this location is: "+output+"\nThe earthquake is sever. It can do considerable damage so plan have precaustionary steps ready. RISK is MEDIUM!")



if __name__ == '__main__':
    app.run(debug = True)