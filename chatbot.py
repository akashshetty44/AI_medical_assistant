# chatbot.py

def medical_chatbot(message):
    """
    Simple rule-based medical chatbot.
    """

    if not message:
        return "Please enter your question."

    message = message.lower()

    # Greetings
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! I am your AI Medical Assistant. How can I help you today?"

    # Fever
    elif "fever" in message:
        return (
            "Fever may be caused by infections such as the flu or a common cold. "
            "Stay hydrated, get plenty of rest, and consult a doctor if your fever "
            "is high or lasts more than 2–3 days."
        )

    # Cough
    elif "cough" in message:
        return (
            "A cough can occur due to a cold, allergies, or other conditions. "
            "Drink warm fluids and seek medical advice if it persists for more than "
            "two weeks or is severe."
        )

    # Headache
    elif "headache" in message:
        return (
            "Headaches may result from stress, dehydration, or illness. "
            "Rest, drink water, and consult a healthcare professional if the pain is severe or recurrent."
        )

    # Cold
    elif "cold" in message:
        return (
            "The common cold usually improves with rest, fluids, and symptomatic care. "
            "If symptoms worsen or persist, consult a doctor."
        )

    # COVID
    elif "covid" in message:
        return (
            "COVID-19 symptoms can include fever, cough, fatigue, and loss of smell or taste. "
            "If you suspect COVID-19, follow local health guidance and consult a healthcare professional."
        )

    # Diabetes
    elif "diabetes" in message:
        return (
            "Diabetes is a condition that affects blood sugar regulation. "
            "Healthy eating, exercise, and prescribed medication can help manage it. "
            "Please consult your doctor for diagnosis and treatment."
        )

    # Heart
    elif "heart" in message:
        return (
            "Chest pain, shortness of breath, or pain spreading to the arm or jaw can be signs of a heart emergency. "
            "Seek immediate medical attention if these symptoms occur."
        )

    # Thanks
    elif any(word in message for word in ["thanks", "thank you"]):
        return "You're welcome! Stay healthy and take care."

    # Goodbye
    elif any(word in message for word in ["bye", "goodbye"]):
        return "Goodbye! Wishing you good health."

    # Default response
    return (
        "I'm sorry, I don't have enough information to answer that. "
        "Please consult a qualified healthcare professional for medical advice."
    )
