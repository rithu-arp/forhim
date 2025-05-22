import streamlit as st
import smtplib
from email.message import EmailMessage

# --- CONFIG ---
YOUR_EMAIL = "rithu.amp@gmail.com"
APP_PASSWORD = "hoka esib qbom zdro"  # Use your Gmail App Password

# Set background and layout
st.set_page_config(page_title="For My Love ❤️", layout="centered")

page_bg_img = f"""
<style>
body {{
background-image: url("https://i.pinimg.com/originals/0a/f6/2f/0af62f8a5f0f6bbfb11b41d408942d07.jpg");
background-size: cover;
background-attachment: fixed;
color: #fff;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Hey Love ❤️")
st.markdown("Let’s talk about your day 🫶")

# Sidebar navigation
page = st.sidebar.radio("Navigate 💌", ["1. Your Mood Today", "2. What You Want to Say", "3. Freebie Request"])

# Session state to store inputs
if "mood" not in st.session_state:
    st.session_state["mood"] = []
if "message" not in st.session_state:
    st.session_state["message"] = ""
if "freebies" not in st.session_state:
    st.session_state["freebies"] = []

# Page 1
if page == "1. Your Mood Today":
    st.subheader("How are you feeling lately, darling? 🥺")
    st.session_state["mood"] = st.multiselect(
        "Choose all that apply 💭",
        ["Happy 😊", "Stressed 😞", "Missing you 😢", "Tired 😴", "Excited 🤩"],
        default=st.session_state["mood"]
    )

# Page 2
elif page == "2. What You Want to Say":
    st.subheader("Tell me whatever’s on your mind 💬")
    st.session_state["message"] = st.text_area("Type here honey...", value=st.session_state["message"], height=200)

# Page 3
elif page == "3. Freebie Request":
    st.subheader("What do you want from me? 🎁")
    st.session_state["freebies"] = st.multiselect(
        "Pick your freebies 🎀",
        ["Hug 🤗", "Kiss 😘", "Date 🍦", "Call 📞", "Cute Photo 📸", "Surprise Gift 🎁"],
        default=st.session_state["freebies"]
    )

    if st.button("Submit All 💌"):
        # Format email
        msg = EmailMessage()
        msg['Subject'] = "A Love Letter Response 💞"
        msg['From'] = YOUR_EMAIL
        msg['To'] = YOUR_EMAIL  # You can also cc to your boyfriend

        content = f"""
        💖 Mood Today:
        {', '.join(st.session_state['mood']) or 'Not shared'}

        📝 Message:
        {st.session_state['message'] or 'No message'}

        🎁 Freebies Requested:
        {', '.join(st.session_state['freebies']) or 'None'}
        """
        msg.set_content(content)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(YOUR_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)
            st.success("Yayy! Your responses were sent to me 💌 Will read it with all my heart!")
        except Exception as e:
            st.error(f"Oops, couldn't send email 😢\n{e}")
