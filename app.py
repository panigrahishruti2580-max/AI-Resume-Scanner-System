import streamlit as st
import pandas as pd

from resume_parser import extract_text
from skill_extractor import extract_skills

from matcher import (
    calculate_match_score,
    missing_skills
)

from semantic_match import semantic_score

from profile_extractor import (
    extract_name,
    extract_email,
    extract_phone
)

from ai_analyzer import (
    generate_summary,
    strengths_weaknesses,
    ai_recommendation,
    interview_questions
)

from charts import (
    radar_chart,
    skill_match_chart
)

from report import generate_report

from candidate_ranker import rank_candidates


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Resume Screening",
    layout="wide"
)

st.title("📄 AI Resume Screening System")


# =====================================
# INPUTS
# =====================================

resume_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description"
)


# =====================================
# MAIN ANALYSIS
# =====================================

if resume_files and job_description:

    # -----------------------------
    # Resume Selector
    # -----------------------------

    selected_resume = st.selectbox(
        "Select Resume For Analysis",
        [file.name for file in resume_files]
    )

    selected_file = None

    for file in resume_files:
        if file.name == selected_resume:
            selected_file = file
            break

    if selected_file:

        selected_file.seek(0)

        resume_text = extract_text(
            selected_file
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            job_description
        )

        keyword_score = calculate_match_score(
            resume_skills,
            jd_skills
        )

        ai_score = semantic_score(
            resume_text,
            job_description
        )

        matched = list(
            set(resume_skills)
            &
            set(jd_skills)
        )

        missing = missing_skills(
            resume_skills,
            jd_skills
        )

        skill_match = 0

        if len(jd_skills) > 0:
            skill_match = (
                len(matched)
                /
                len(jd_skills)
            ) * 100

        final_score = (
            keyword_score * 0.6
            +
            ai_score * 0.4
        )

        recommendation = ai_recommendation(
            final_score
        )

        # =====================================
        # TABS
        # =====================================

        tabs = st.tabs([
            "Overview",
            "Profile",
            "AI Analysis",
            "Charts",
            "Interview Questions",
            "Resume",
            "Candidate Ranking"
        ])

        # =====================================
        # OVERVIEW
        # =====================================

        with tabs[0]:

            st.subheader("📊 Matching Scores")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Keyword Score",
                    f"{keyword_score:.2f}%"
                )

            with col2:
                st.metric(
                    "AI Similarity",
                    f"{ai_score:.2f}%"
                )

            st.subheader("Recommendation")

            st.markdown(
                recommendation
            )

            report = generate_report(
                keyword_score,
                ai_score,
                matched,
                missing,
                recommendation
            )

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="candidate_report.txt",
                mime="text/plain"
            )

            rows = []

            for skill in jd_skills:

                rows.append({
                    "Skill": skill,
                    "Status":
                        "Matched"
                        if skill in resume_skills
                        else "Missing"
                })

            st.subheader(
                "Skill Gap Analysis"
            )

            st.dataframe(
                pd.DataFrame(rows),
                use_container_width=True
            )

        # =====================================
        # PROFILE
        # =====================================

        with tabs[1]:

            st.subheader(
                "👤 Candidate Profile"
            )

            st.write(
                "Name:",
                extract_name(
                    resume_text
                )
            )

            st.write(
                "Email:",
                extract_email(
                    resume_text
                )
            )

            st.write(
                "Phone:",
                extract_phone(
                    resume_text
                )
            )

        # =====================================
        # AI ANALYSIS
        # =====================================

        with tabs[2]:

            st.markdown(
                generate_summary(
                    resume_skills,
                    keyword_score,
                    ai_score
                )
            )

            st.markdown(
                strengths_weaknesses(
                    matched,
                    missing
                )
            )

        # =====================================
        # CHARTS
        # =====================================

        with tabs[3]:

            st.subheader(
                "📈 Analytics Dashboard"
            )

            fig1 = radar_chart(
                keyword_score,
                ai_score,
                skill_match
            )

            st.plotly_chart(
                fig1,
                use_container_width=True
            )

            fig2 = skill_match_chart(
                len(matched),
                len(missing)
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        # =====================================
        # INTERVIEW QUESTIONS
        # =====================================

        with tabs[4]:

            st.subheader(
                "🎯 Suggested Interview Questions"
            )

            questions = interview_questions(
                resume_skills
            )

            for q in questions:
                st.write("•", q)

        # =====================================
        # RESUME
        # =====================================

        with tabs[5]:

            st.subheader(
                "📄 Resume Content"
            )

            st.text_area(
                "Resume Text",
                resume_text,
                height=500
            )

        # =====================================
        # CANDIDATE RANKING
        # =====================================

        with tabs[6]:

            st.subheader(
                "🏆 Candidate Ranking"
            )

            if len(resume_files) > 1:

                rankings = rank_candidates(
                    resume_files,
                    job_description
                )

                if len(rankings) > 0:

                    ranking_df = pd.DataFrame(
                        rankings
                    )

                    ranking_df.insert(
                        0,
                        "Rank",
                        range(
                            1,
                            len(ranking_df) + 1
                        )
                    )

                    st.dataframe(
                        ranking_df,
                        use_container_width=True
                    )

                    top_candidate = rankings[0]

                    st.success(
                        f"""
🏆 Top Candidate

Candidate: {top_candidate['Candidate']}

Final Score: {top_candidate['Final Score']}%
"""
                    )

                else:

                    st.warning(
                        "No ranking data generated."
                    )

            else:

                st.info(
                    "Upload at least 2 resumes to view candidate ranking."
                )

else:

    st.info(
        "Upload resume(s) and paste a job description to begin."
    )