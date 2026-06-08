def generate_summary(
    resume_skills,
    keyword_score,
    ai_score
):

    summary = f"""
## Candidate Summary

The candidate demonstrates skills in:

{', '.join(resume_skills)}

Keyword Match Score: {keyword_score}%

AI Similarity Score: {ai_score}%

Overall the candidate possesses relevant technical competencies.
"""

    return summary


def strengths_weaknesses(
    matched_skills,
    missing_skills_list
):

    report = "## Strengths\n\n"

    if matched_skills:

        for skill in matched_skills:
            report += f"✅ {skill}\n"

    else:

        report += "No major strengths identified.\n"

    report += "\n## Weaknesses\n\n"

    if missing_skills_list:

        for skill in missing_skills_list:
            report += f"❌ {skill}\n"

    else:

        report += "No major weaknesses detected.\n"

    return report


def ai_recommendation(
    final_score
):

    if final_score >= 80:

        return """
## Recommendation

🟢 Strong Match

Candidate is recommended for interview.
"""

    elif final_score >= 60:

        return """
## Recommendation

🟡 Moderate Match

Candidate should be reviewed manually.
"""

    else:

        return """
## Recommendation

🔴 Low Match

Candidate does not sufficiently match the role.
"""


def interview_questions(
    skills
):

    questions = []

    mapping = {

        "python": [
            "Explain Python decorators.",
            "What are generators in Python?"
        ],

        "sql": [
            "Difference between JOIN and UNION?",
            "Explain indexing in SQL."
        ],

        "machine learning": [
            "What is overfitting?",
            "Explain bias variance tradeoff."
        ],

        "aws": [
            "Explain EC2.",
            "Difference between EC2 and Lambda?"
        ],

        "docker": [
            "What is containerization?",
            "Difference between Docker and Virtual Machine?"
        ],

        "power bi": [
            "What are DAX functions?",
            "Explain Power BI dashboards."
        ],

        "tableau": [
            "What are calculated fields?",
            "How does Tableau connect to data?"
        ],

        "pandas": [
            "How do you handle missing values?",
            "Difference between loc and iloc?"
        ]
    }

    for skill in skills:

        if skill in mapping:

            questions.extend(
                mapping[skill]
            )

    if not questions:

        questions.append(
            "Tell me about your most challenging project."
        )

    return questions[:10]