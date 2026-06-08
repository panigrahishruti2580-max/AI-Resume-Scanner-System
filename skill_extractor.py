skills_db = [

    # Programming
    "python",
    "java",
    "javascript",
    "sql",

    # Data Analysis
    "pandas",
    "numpy",
    "statistics",
    "data analysis",
    "data modeling",

    # Visualization
    "power bi",
    "tableau",
    "excel",

    # Machine Learning
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "nlp",

    # Database
    "mongodb",
    "postgresql",
    "mysql",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",

    # Analytics
    "etl",
    "business intelligence",
    "predictive analytics"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))