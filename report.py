def generate_report(
    keyword_score,
    ai_score,
    matched,
    missing,
    recommendation
):

    return f"""
AI RESUME SCREENING REPORT

Keyword Score:
{keyword_score}%

AI Similarity:
{ai_score}%

Recommendation:
{recommendation}

Matched Skills:
{', '.join(matched)}

Missing Skills:
{', '.join(missing)}
"""