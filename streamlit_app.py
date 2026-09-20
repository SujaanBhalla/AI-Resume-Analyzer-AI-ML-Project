import streamlit as st
import os
import tempfile

from app.parser import parse_resume
from app.ats import calculate_ats_score
from app.career import predict_career


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
}

.block-container {
    max-width: 1200px;
    padding-top: 45px;
    padding-bottom: 40px;
}

.hero {
    text-align: center;
    padding: 20px 20px 35px 20px;
}

.hero h1 {
    color: white;
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 15px;
}

.hero p {
    color: #dbeafe;
    font-size: 18px;
    line-height: 1.7;
    max-width: 750px;
    margin: auto;
}

.upload-card {
    background: rgba(255,255,255,0.10);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 35px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.30);
    text-align: center;
}

.upload-card h2 {
    color: white;
    font-size: 28px;
}

.upload-card p {
    color: #dbeafe;
}

.section-title {
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: 600;
    margin: 45px 0 25px 0;
}

.feature-card {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 28px;
    min-height: 210px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

.feature-card h3 {
    color: white;
    font-size: 20px;
    margin-bottom: 15px;
}

.feature-card p {
    color: #dbeafe;
    line-height: 1.7;
    font-size: 15px;
}

.metric-card {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}

.metric-card h2 {
    color: white;
    font-size: 32px;
}

.metric-card p {
    color: #dbeafe;
}

.skill-badge {
    display: inline-block;
    background: rgba(37,99,235,0.80);
    color: white;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 20px;
    font-size: 14px;
}

.role-card {
    background: rgba(255,255,255,0.09);
    border-radius: 14px;
    padding: 16px;
    margin-bottom: 10px;
    color: white;
}

.footer {
    text-align: center;
    color: #cbd5e1;
    margin-top: 50px;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <div class="hero">
        <h1>🤖 AI Resume Analyzer</h1>
        <p>
            Upload your resume and get AI-powered analysis,
            ATS score evaluation, skill insights,
            and personalized career recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="upload-card">
        <h2>📄 Upload Your Resume</h2>
        <p>
            Upload your resume in PDF format to analyze your profile.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"],
    help="PDF • Maximum 200MB"
)


if uploaded_file is not None:

    st.write(f"📄 Selected file: **{uploaded_file.name}**")

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    ):

        temp_file_path = None

        try:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as temp_file:

                temp_file.write(
                    uploaded_file.getbuffer()
                )

                temp_file_path = temp_file.name

            with st.spinner(
                "Analyzing your resume..."
            ):

                resume_data = parse_resume(
                    temp_file_path
                )

                ats_score = calculate_ats_score(
                    resume_data
                )

                skills = resume_data.get(
                    "Skills",
                    []
                )

                career = predict_career(
                    skills
                )

            st.success(
                "Resume analyzed successfully! 🎉"
            )

            st.markdown(
                "## 📊 Resume Analysis Report"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <h2>{ats_score}%</h2>
                        <p>⭐ ATS Score</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col2:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <h2>{len(skills)}</h2>
                        <p>🛠 Skills Found</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with col3:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <h2>{career["score"]}%</h2>
                        <p>💼 Career Match</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("### 👤 Resume Information")

            col1, col2 = st.columns(2)

            with col1:
                st.write(
                    f"**Name:** "
                    f"{resume_data.get('Name', 'Not Found')}"
                )

                st.write(
                    f"**Email:** "
                    f"{resume_data.get('Email', 'Not Found')}"
                )

            with col2:
                st.write(
                    f"**Phone:** "
                    f"{resume_data.get('Phone', 'Not Found')}"
                )

                st.write(
                    f"**File:** "
                    f"{uploaded_file.name}"
                )

            st.markdown("### 🛠 Technical Skills")

            if skills:

                skill_html = ""

                for skill in skills:
                    skill_html += (
                        f'<span class="skill-badge">'
                        f'{skill}'
                        f'</span>'
                    )

                st.markdown(
                    skill_html,
                    unsafe_allow_html=True
                )

            else:
                st.write(
                    "No technical skills detected."
                )

            st.markdown("### 💼 Career Prediction")

            st.success(
                f"Recommended Career: {career['role']}"
            )

            st.write(
                f"Match Confidence: "
                f"**{career['score']}%**"
            )

            st.progress(
                career["score"] / 100
            )

            st.markdown("### Top Career Options")

            for role in career["top_roles"]:

                st.markdown(
                    f"""
                    <div class="role-card">
                        <strong>{role["role"]}</strong>
                        <span style="float:right;">
                            {role["score"]}%
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.progress(
                    role["score"] / 100
                )

            st.markdown("### 🤖 AI Resume Suggestions")

            st.info(
                "Add more project details"
            )

            st.info(
                "Mention measurable achievements"
            )

            st.info(
                "Keep skills updated according to job role"
            )

            st.info(
                "Use relevant keywords for ATS optimization"
            )

            with st.expander(
                "📄 View Raw Resume Data"
            ):
                st.json(resume_data)

        except Exception as e:

            st.error(
                f"Something went wrong: {str(e)}"
            )

        finally:

            if (
                temp_file_path
                and os.path.exists(temp_file_path)
            ):
                os.remove(
                    temp_file_path
                )


st.markdown(
    '<div class="section-title">✨ What This Tool Does</div>',
    unsafe_allow_html=True
)


feature1, feature2, feature3, feature4 = st.columns(4)


with feature1:

    st.markdown(
        """
        <div class="feature-card">
            <h3>⭐ ATS Score Analysis</h3>
            <p>
                Analyze your resume compatibility
                with Applicant Tracking Systems
                and improve your chances of selection.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with feature2:

    st.markdown(
        """
        <div class="feature-card">
            <h3>💼 Career Prediction</h3>
            <p>
                Get recommended career paths
                based on your skills,
                technologies, and profile.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with feature3:

    st.markdown(
        """
        <div class="feature-card">
            <h3>🧠 Skill Extraction</h3>
            <p>
                Automatically detect technical skills
                and identify your professional strengths.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with feature4:

    st.markdown(
        """
        <div class="feature-card">
            <h3>📈 Resume Improvement</h3>
            <p>
                Receive AI-based suggestions
                to improve your resume quality.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    """
    <div class="footer">
        Built using Python • Streamlit • NLP •
        Machine Learning • AI
    </div>
    """,
    unsafe_allow_html=True
)