import streamlit as st

st.set_page_config(
    page_title="Wedding Choice 💍",
    page_icon="💒",
    layout="centered"
)

st.markdown(
    """
    <h1 style="text-align:center; color:#e75480;">
        Which wedding would you like to attend? 💍✨
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- INITIALIZE SESSION STATE ----------------
if "votes" not in st.session_state:
    st.session_state.votes = {
        "Kutubuddin weds Sahubuddin": 0,
        "Trishu weds Sudarshan": 0,
        "Pratu weds Dheeru": 0,
        "Shikhu weds Punyak baniyan": 0
    }

if "has_voted" not in st.session_state:
    st.session_state.has_voted = False

if "selected" not in st.session_state:
    st.session_state.selected = None


# ---------------- BUTTON GRID (2 x 2) ----------------
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

with row1_col1:
    if st.button(
        "💐 Kutubuddin weds Sahubuddin",
        use_container_width=True,
        disabled=st.session_state.has_voted
    ):
        st.session_state.votes["Kutubuddin weds Sahubuddin"] += 1
        st.session_state.selected = "Kutubuddin weds Sahubuddin"
        st.session_state.has_voted = True

with row1_col2:
    if st.button(
        "💖 Trishu weds Sudarshan",
        use_container_width=True,
        disabled=st.session_state.has_voted
    ):
        st.session_state.votes["Trishu weds Sudarshan"] += 1
        st.session_state.selected = "Trishu weds Sudarshan"
        st.session_state.has_voted = True

with row2_col1:
    if st.button(
        "🌸 Pratu weds Dheeru",
        use_container_width=True,
        disabled=st.session_state.has_voted
    ):
        st.session_state.votes["Pratu weds Dheeru"] += 1
        st.session_state.selected = "Pratu weds Dheeru"
        st.session_state.has_voted = True

with row2_col2:
    if st.button(
        "💍 Shikhu weds Punyak baniyan",
        use_container_width=True,
        disabled=st.session_state.has_voted
    ):
        st.session_state.votes["Shikhu weds Punyak baniyan"] += 1
        st.session_state.selected = "Shikhu weds Punyak baniyan"
        st.session_state.has_voted = True


# ---------------- LIVE COUNTS ----------------
st.write("")
st.subheader("📊 Live Attendance Count")

for wedding, count in st.session_state.votes.items():
    st.write(f"• **{wedding}** : {count}")


# ---------------- CONFIRMATION ----------------
if st.session_state.has_voted:
    st.success(f"🎉 You voted for **{st.session_state.selected}**!")
    st.balloons()
