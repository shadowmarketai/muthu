import streamlit as st

# 🎨 Page Config
st.set_page_config(page_title="🌟 Multi-Prompt Grading Dashboard", layout="wide")

st.title("📊 **Multi-Prompt Grading Rubric**")
st.caption("✨ *Review and rate multiple AI prompt outputs in one place!*")

# 📝 Example prompt outputs
prompts = [
    {
        "title": "🏡 Villa Automation Advice",
        "thought": "Imagine you're designing an ultra-modern villa where every detail speaks luxury. You need to assess smart home systems for mood lighting, energy optimization, and seamless control using voice and mobile apps.",
        "output": """
Thought:
For a luxury villa, focus on scalability, intuitive controls, energy efficiency, and integration with premium AV systems.

Action:
Shortlist systems like Crestron, Control4, and KNX which are known for high-end automation.

Observation:
Crestron excels in lighting scenes, Control4 offers great AV integration, KNX is highly modular.

Answer:
For a premium 4BHK villa in Coimbatore, Crestron or Control4 paired with Cinespa’s custom design will ensure a blend of elegance, technology, and comfort.
"""
    },
    {
        "title": "🌱 Sustainable Farming Tips",
        "thought": "You are advising a farmer who wants to transition to sustainable agriculture. Suggest practices that improve yield without harming the ecosystem.",
        "output": """
Thought:
The focus is on eco-friendly techniques, soil health, and biodiversity.

Action:
Suggest crop rotation, organic fertilizers, drip irrigation, and companion planting.

Observation:
These methods reduce chemical use, conserve water, and improve long-term soil fertility.

Answer:
Implement crop rotation and drip irrigation first for quick impact, then transition to organic pest control and companion planting.
"""
    },
    {
        "title": "📱 Mobile App Monetization",
        "thought": "Imagine you’re helping a startup choose the best strategy to monetize their productivity app. Consider user experience and long-term growth.",
        "output": """
Thought:
Key priorities are user retention, value delivery, and scalability.

Action:
Evaluate freemium, subscription models, and in-app purchases.

Observation:
Freemium draws users quickly but may limit revenue, subscriptions offer steady income, in-app purchases work best for feature-heavy apps.

Answer:
Start with freemium to build a user base, then transition to tiered subscriptions for long-term monetization.
"""
    }
]

# 🌟 Grading Criteria
criteria = ["Relevance 🎯", "Accuracy ✅", "Clarity 🔍", "Fluency 🌊", "Creativity 💡"]
weights = {"Relevance 🎯": 3, "Accuracy ✅": 3, "Clarity 🔍": 2, "Fluency 🌊": 1, "Creativity 💡": 1}

# 🚀 Multi-Prompt Grading UI
for i, prompt in enumerate(prompts, start=1):
    with st.expander(f"{prompt['title']}"):
        st.markdown(f"### 🧠 **Thought:** {prompt['thought']}")
        st.code(prompt['output'], language="markdown")

        st.markdown("### 📝 **Rate this output**")
        scores = {}
        for criterion in criteria:
            score = st.radio(
                f"Rate {criterion}",
                [1, 2, 3, 4, 5],
                format_func=lambda x: "⭐" * x,
                horizontal=True,
                key=f"{i}_{criterion}"
            )
            scores[criterion] = score

        # 🎯 Weighted Score Calculation
        weighted_total = sum(scores[c] * weights[c] for c in scores)
        max_total = sum(5 * weights[c] for c in scores)
        final_score = (weighted_total / max_total) * 100

        # 🎨 Display Final Grade
        if final_score >= 85:
            st.success(f"🌟 Excellent: {final_score:.1f}%")
        elif final_score >= 70:
            st.info(f"👍 Good: {final_score:.1f}%")
        elif final_score >= 50:
            st.warning(f"⚠️ Needs Improvement: {final_score:.1f}%")
        else:
            st.error(f"❌ Poor: {final_score:.1f}%")

        # 🏷️ Strengths & Weaknesses
        strengths = st.multiselect(
            f"✅ Strengths for {prompt['title']}",
            ["Well-structured", "Creative approach", "Clear language", "Strong logic"]
        )
        weaknesses = st.multiselect(
            f"⚠️ Weaknesses for {prompt['title']}",
            ["Too generic", "Inaccurate details", "Repetitive", "Lacks originality"]
        )
        st.text_area(f"💬 Additional Feedback for {prompt['title']}")

st.markdown("---")
st.info("✅ *All prompts reviewed! Thanks for grading.*")

# 👣 Floating Footer
from muthu_footer import add_footer
add_footer()
