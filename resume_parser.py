# AI Resume Analyzer
# Extracts PDF text and analyzes candidate skills



from PyPDF2 import PdfReader



def extract_text(file):

    reader = PdfReader(file)

    text = ""


    for page in reader.pages:

        text += page.extract_text()


    return text





def analyze_resume(text):


    skills = [

        "python",
        "machine learning",
        "data science",
        "html",
        "css",
        "javascript",
        "sql",
        "flask"

    ]


    found = []


    missing = []



    text = text.lower()



    for skill in skills:


        if skill in text:

            found.append(skill)

        else:

            missing.append(skill)

# Calculate resume score based on matched skills

    score = int(
        (len(found) / len(skills)) * 100
    )

# Generate learning recommendations for missing skills

    recommendations = []


    for skill in missing:

        recommendations.append(
            "Learn " + skill
        )



    return {


        "score": score,


        "found": found,


        "missing": missing,


        "recommendations": recommendations


    }