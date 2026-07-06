# symptom_checker.py

import difflib

# List of supported symptoms
VALID_SYMPTOMS = [
    "fever",
    "cough",
    "headache",
    "sore throat",
    "runny nose",
    "fatigue",
    "body pain",
    "chills",
    "vomiting",
    "sweating",
    "stomach pain",
    "weakness",
    "loss of appetite",
    "loss of smell",
    "breathing difficulty",
    "diarrhea",
    "nausea",
    "dizziness",
    "chest pain",
    "joint pain"
]


def normalize_symptom(symptom):
    """
    Convert symptom to lowercase and remove extra spaces.
    """
    return symptom.lower().strip()


def validate_symptoms(symptom_list):
    """
    Validate symptoms entered by the user.

    Returns:
        valid_symptoms (list)
        invalid_symptoms (list)
    """

    valid = []
    invalid = []

    for symptom in symptom_list:

        symptom = normalize_symptom(symptom)

        if symptom in VALID_SYMPTOMS:
            valid.append(symptom)
        else:
            invalid.append(symptom)

    return valid, invalid


def suggest_symptom(symptom):
    """
    Suggest the closest matching symptom.
    """

    symptom = normalize_symptom(symptom)

    matches = difflib.get_close_matches(
        symptom,
        VALID_SYMPTOMS,
        n=1,
        cutoff=0.6
    )

    if matches:
        return matches[0]

    return None


def check_symptoms(symptom_list):
    """
    Validate symptoms and provide suggestions.
    """

    valid, invalid = validate_symptoms(symptom_list)

    suggestions = {}

    for symptom in invalid:

        suggestion = suggest_symptom(symptom)

        if suggestion:
            suggestions[symptom] = suggestion

    return {
        "valid_symptoms": valid,
        "invalid_symptoms": invalid,
        "suggestions": suggestions
    }


# Test
if __name__ == "__main__":

    symptoms = [
        "Fever",
        "Cogh",
        "Headache",
        "Vomitting",
        "Cold"
    ]

    result = check_symptoms(symptoms)

    print("Valid Symptoms:")
    print(result["valid_symptoms"])

    print("\nInvalid Symptoms:")
    print(result["invalid_symptoms"])

    print("\nSuggestions:")
    for wrong, correct in result["suggestions"].items():
        print(f"{wrong} -> {correct}")
