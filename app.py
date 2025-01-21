from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

clf = None  # To hold the trained classifier

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global clf
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Load and process data
        df = pd.read_csv(filepath)
        df.loc[df['Downtime'] == 'Machine_Failure', 'Downtime'] = 1
        df.loc[df['Downtime'] == 'No_Machine_Failure', 'Downtime'] = 0
        df = df.iloc[:, 3:]
        df = df.astype(float)
        df = df.fillna(df.mean())

        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        # Train/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

        # Train model
        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)

        # Evaluate model
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        pre = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)

        return jsonify({
            "message": "Model trained successfully",
            "accuracy": acc,
            "precision": pre,
            "recall": rec
        })

@app.route('/predict', methods=['POST'])
def predict():
    global clf
    if clf is None:
        return "Model not trained yet. Please upload data to train the model."

    data = request.get_json()
    if not data:
        return "Invalid input. Please provide JSON data."

    try:
        input_data = pd.DataFrame([data])
        prediction = int(clf.predict(input_data.values)[0])
        result = "Machine Failure" if prediction == 1 else "No Machine Failure"

        return jsonify({
            "prediction": result
        })
    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
