# medicine_info.py

MEDICINES = {
    "paracetamol": {
        "uses": "Helps reduce fever and relieve mild to moderate pain.",
        "dosage": "Use only as directed on the label or by a healthcare professional.",
        "side_effects": [
            "Nausea",
            "Skin rash (rare)",
            "Liver damage if taken in excessive amounts"
        ]
    },

    "ibuprofen": {
        "uses": "Helps reduce pain, inflammation, and fever.",
        "dosage": "Take with food and follow the recommended dosage.",
        "side_effects": [
            "Stomach pain",
            "Heartburn",
            "Nausea"
        ]
    },

    "cetirizine": {
        "uses": "Relieves allergy symptoms such as sneezing, itching, and runny nose.",
        "dosage": "Use only as directed on the label or by a healthcare professional.",
        "side_effects": [
            "Drowsiness",
            "Dry mouth",
            "Fatigue"
        ]
    },

    "omeprazole": {
        "uses": "Reduces stomach acid and helps treat acidity and ulcers.",
        "dosage": "Usually taken before meals as directed by a healthcare professional.",
        "side_effects": [
            "Headache",
            "Stomach pain",
            "Diarrhea"
        ]
    },

    "ors": {
        "uses": "Helps replace fluids and electrolytes lost due to diarrhea or vomiting.",
        "dosage": "Prepare and use according to the packet instructions.",
        "side_effects": [
            "Generally safe when used correctly."
        ]
    }
}


def get_medicine_info(medicine_name):
    """
    Returns information about a medicine.
    """

    medicine_name = medicine_name.lower().strip()

    if medicine_name in MEDICINES:
        return MEDICINES[medicine_name]

    return {
        "uses": "Medicine not found in the database.",
        "dosage": "Consult a pharmacist or doctor.",
        "side_effects": [
            "Information unavailable."
        ]
    }


# Test
if __name__ == "__main__":

    medicine = input("Enter medicine name: ")

    info = get_medicine_info(medicine)

    print("\nMedicine:", medicine.title())
    print("Uses:", info["uses"])
    print("Dosage:", info["dosage"])
    print("Possible Side Effects:")

    for effect in info["side_effects"]:
        print("-", effect)
