import streamlit as st


st.set_page_config(
    page_title="EMI Burden Analyzer",
    page_icon=":money_with_wings:",
    layout="wide",
)


def get_stress_band(emi_ratio: float) -> tuple[str, str, str]:
    if emi_ratio < 20:
        return (
            "Comfortable",
            "Your current EMI load is generally manageable.",
            "#0f9d58",
        )
    if emi_ratio < 35:
        return (
            "Caution",
            "You still have room, but new debt should be considered carefully.",
            "#f4b400",
        )
    if emi_ratio < 50:
        return (
            "Stretched",
            "A large share of income is already committed to existing debt.",
            "#f57c00",
        )
    return (
        "High Risk",
        "Your EMI burden is heavy and may affect loan eligibility.",
        "#db4437",
    )


def format_inr(value: float) -> str:
    return f"Rs. {value:,.0f}"


st.title("EMI Burden Analyzer")
st.caption("A practical check to see whether your existing EMI load is financially comfortable.")

with st.sidebar:
    st.header("Input Details")
    monthly_salary = st.number_input(
        "Monthly salary",
        min_value=1_000,
        value=60_000,
        step=1_000,
    )
    current_emis = st.number_input(
        "Total current monthly EMIs",
        min_value=0,
        value=15_000,
        step=500,
    )
    loan_tenure_months = st.slider(
        "Remaining loan tenure (months)",
        min_value=1,
        max_value=360,
        value=60,
        step=1,
    )


emi_ratio = (current_emis / monthly_salary) * 100 if monthly_salary else 0
stress_level, stress_message, stress_color = get_stress_band(emi_ratio)
post_emi_income = monthly_salary - current_emis
total_remaining_outflow = current_emis * loan_tenure_months

st.markdown(
    f"""
    <div style="padding: 1rem 1.2rem; border-radius: 16px; background: linear-gradient(135deg, {stress_color}18, #f8fafc); border: 1px solid {stress_color}55;">
        <h3 style="margin: 0; color: {stress_color};">Financial Stress Level: {stress_level}</h3>
        <p style="margin: 0.5rem 0 0 0; font-size: 1rem;">{stress_message}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
col1.metric("EMI-to-Income Ratio", f"{emi_ratio:.1f}%")
col2.metric("Income Left After EMIs", format_inr(post_emi_income))
col3.metric("Projected EMI Outflow", format_inr(total_remaining_outflow))

st.subheader("What This Means")

if emi_ratio < 20:
    st.success("This is usually seen as a healthy EMI burden for most salaried borrowers.")
elif emi_ratio < 35:
    st.info("This is still workable, but lenders may look closely at any new loan request.")
elif emi_ratio < 50:
    st.warning("Your repayment load is on the higher side and can limit fresh borrowing capacity.")
else:
    st.error("This level can signal significant repayment pressure and weaker loan approval chances.")

st.subheader("Quick Summary")
st.write(
    f"You earn **{format_inr(monthly_salary)}** per month and already pay "
    f"**{format_inr(current_emis)}** in EMIs. That means **{emi_ratio:.1f}%** "
    "of your salary is committed to existing debt."
)
st.write(
    f"If this EMI continues for the next **{loan_tenure_months} months**, the remaining repayment "
    f"outflow will be about **{format_inr(total_remaining_outflow)}**."
)

st.subheader("Typical Interpretation Used by Lenders")
st.write(
    """
    - Below 20%: Very comfortable
    - 20% to 35%: Usually acceptable
    - 35% to 50%: Higher stress
    - Above 50%: Risky for new borrowing
    """
)
