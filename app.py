from flask import Flask, render_template, request, jsonify
from disease_prediction import predict_disease
from chatbot import medical_chatbot
from database import create_database, save_patient

app = Flask(__name__)

# Create database when application starts
create_database()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')

    symptoms = [
        request.form.get('symptom1'),
        request.form.get('symptom2'),
        request.form.get('symptom3'),
        request.form.get('symptom4'),
        request.form.get('symptom5')
    ]

    symptoms = [s for s in symptoms if s]

    disease, precautions = predict_disease(symptoms)

    save_patient(
        name,
        age,
        gender,
        ",".join(symptoms),
        disease
    )

    return render_template(
        'result.html',
        name=name,
        age=age,
        gender=gender,
        symptoms=symptoms,
        disease=disease,
        precautions=precautions
    )


@app.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()

    message = data.get("message")

    reply = medical_chatbot(message)

    return jsonify({
        "reply": reply
    })


@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")


if __name__ == "__main__":
    app.run(debug=True)
