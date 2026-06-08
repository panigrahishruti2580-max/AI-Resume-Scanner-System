import streamlit as st

st.error("🔥 CANDIDATE_RANKER FILE LOADED 🔥")

from resume_parser import extract_text
from skill_extractor import extract_skills
from matcher import calculate_match_score
from semantic_match import semantic_score


def rank_candidates(resume_files, job_description):

    candidates = []

    jd_skills = extract_skills(job_description)

    st.write("DEBUG → Total Uploaded Files:", len(resume_files))

    for file in resume_files:

        st.write("━━━━━━━━━━━━━━━━━━━━")
        st.write("Processing Resume:", file.name)

        try:

            file.seek(0)

            resume_text = extract_text(file)

            st.write("Text Length:", len(resume_text))

            if not resume_text.strip():

                st.error(
                    f"No text extracted from {file.name}"
                )

                continue

            resume_skills = extract_skills(
                resume_text
            )

            st.write(
                "Skills Found:",
                resume_skills
            )

            keyword_score = calculate_match_score(
                resume_skills,
                jd_skills
            )

            st.write(
                "Keyword Score:",
                keyword_score
            )

            ai_score = semantic_score(
                resume_text,
                job_description
            )

            st.write(
                "AI Score:",
                ai_score
            )

            final_score = (
                float(keyword_score) * 0.6
                + float(ai_score) * 0.4
            )

            st.write(
                "Final Score:",
                final_score
            )

            candidates.append({
                "Candidate": file.name,
                "Keyword Score": round(float(keyword_score), 2),
                "AI Score": round(float(ai_score), 2),
                "Final Score": round(float(final_score), 2)
            })

            st.success(
                f"Added Candidate: {file.name}"
            )

        except Exception as e:

            st.error(
                f"Error processing {file.name}"
            )

            st.exception(e)

    st.write(
        "DEBUG → Candidates Added:",
        len(candidates)
    )

    st.write("FINAL CANDIDATE LIST:")
    st.json(candidates)

    candidates = sorted(
        candidates,
        key=lambda x: x["Final Score"],
        reverse=True
    )

    return candidates