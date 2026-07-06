# disease_prediction.py

# Disease database
DISEASE_DATA = {
    "Common Cold": {
        "symptoms": [
            "fever",
            "cough",
            "sore throat",
            "runny nose",
            "headache"
        ],
        "precautions": [
            "Drink plenty of fluids",
            "Take adequate rest",
            "Use steam inhalation",
            "Consult a doctor if symptoms persist"
        ]
    },

    "Flu": {
        "symptoms": [
            "fever",
            "cough",
            "body pain",
            "fatigue",
            "chills"
        ],
        "precautions": [
            "Rest well",
            "Drink warm fluids",
            "Take medicines prescribed by a doctor",
            "Monitor body temperature"
        ]
    },

    "Malaria": {
        "symptoms": [
            "fever",
            "chills",
            "vomiting",
            "headache",
            "sweating"
        ],
        "precautions": [
            "Get a blood test",
            "Consult a doctor immediately",
            "Stay hydrated",
            "Take prescribed antimalarial medicine"
        ]
    },

    "Typhoid": {
        "symptoms": [
            "fever",
            "stomach pain",
            "weakness",
            "headache",
            "loss of appetite"
        ],
        "precautions": [
            "Drink boiled water",
            "Take antibiotics only if prescribed",
            "Eat light food",
            "Take adequate rest"
        ]
    },

    "COVID-19": {
        "symptoms": [
            "fever",
            "cough",
            "loss of smell",
            "fatigue",
            "breathing difficulty"
        ],
        "precautions": [
            "Wear a mask",
            "Isolate if necessary",
            "Stay hydrated",
            "Seek medical attention if breathing worsens"
        ]
    }
}


def predict_disease(user_symptoms):
    """
    Predict disease based on symptom matching.

    Parameters:
        user_symptoms (list): List of symptoms entered by the user.

    Returns:
        disease (str)
        precautions (list)
    """

    user_symptoms = [s.lower().strip() for s in user_symptoms]

    best_match = None
    highest_score = 0

    for disease, details in DISEASE_DATA.items():

        score = len(
            set(user_symptoms) &
            set([s.lower() for s in details["symptoms"]])
        )

        if score > highest_score:
            highest_score = score
            best_match = disease

    if best_match:
        return best_match, DISEASE_DATA[best_match]["precautions"]

    return (
        "No matching disease found",
        [
            "Consult a healthcare professional.",
            "Do not rely solely on this prediction."
        ]
    )
