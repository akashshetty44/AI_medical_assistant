pip install PyPDF2

# report_analyzer.py

import PyPDF2


# Medical keywords
KEYWORDS = [
    "diabetes",
    "hypertension",
    "blood pressure",
    "hemoglobin",
    "glucose",
    "cholesterol",
    "platelet",
    "creatinine",
    "covid",
    "malaria",
    "dengue",
    "thyroid",
    "fever",
    "infection",
    "heart",
    "kidney",
    "liver"
]


def extract_text(pdf_path):
    """
    Extract text from a PDF file.
    """

    text = ""

    try:
        with open(pdf_path, "rb") as file:

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:
        return f"Error reading PDF: {e}"

    return text


def analyze_report(pdf_path):
    """
    Analyze the medical report and return a summary.
    """

    report_text = extract_text(pdf_path)

    if report_text.startswith("Error"):
        return {
            "error": report_text
        }

    report_lower = report_text.lower()

    detected = []

    for keyword in KEYWORDS:
        if keyword in report_lower:
            detected.append(keyword)

    summary = {
        "keywords_found": detected,
        "total_keywords": len(detected),
        "report_length": len(report_text),
        "message": (
            "Analysis completed. "
            "Please consult a qualified healthcare professional "
            "for interpretation of your report."
        )
    }

    return summary


# Test
if __name__ == "__main__":

    path = input("Enter PDF path: ")

    result = analyze_report(path)

    print("\n----- REPORT SUMMARY -----")

    if "error" in result:
        print(result["error"])

    else:
        print("Keywords Found:")
        for item in result["keywords_found"]:
            print("-", item)

        print("\nTotal Keywords:", result["total_keywords"])
        print("Report Length:", result["report_length"], "characters")
        print(result["message"])
