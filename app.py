import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Trade Opportunities Analyzer", layout="wide")

st.title("📊 Trade Opportunities Analyzer (India)")
st.write("Analyze market opportunities for different sectors using AI")

# 🔐 Login Section
st.sidebar.header("🔐 Login")

username = st.sidebar.text_input("Enter Username")

if st.sidebar.button("Login"):
    if username:
        response = requests.post(f"{BASE_URL}/login", params={"username": username})

        if response.status_code == 200:
            token = response.json()["access_token"]
            st.session_state["token"] = token
            st.sidebar.success("Login successful ✅")
        else:
            st.sidebar.error("Login failed ❌")
    else:
        st.sidebar.warning("Enter username")

# 📌 Sector Input
st.subheader("Enter Sector")
sector = st.text_input("Example: pharmaceuticals, technology, agriculture")

# 🚀 Analyze Button
if st.button("Analyze Sector"):
    if "token" not in st.session_state:
        st.error("⚠️ Please login first")
    elif not sector:
        st.warning("⚠️ Please enter a sector")
    else:
        headers = {
            "Authorization": f"Bearer {st.session_state['token']}"
        }

        with st.spinner("🔍 Analyzing market data..."):
            try:
                response = requests.get(
                    f"{BASE_URL}/analyze/{sector}",
                    headers=headers
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("✅ Analysis Completed")

                    # 📝 Display Markdown
                    st.markdown(data["report"])

                else:
                    st.error(f"Error: {response.text}")

            except Exception as e:
                st.error(f"Connection error: {e}")

# 📊 Session Info
st.sidebar.markdown("---")
st.sidebar.write("ℹ️ Make sure FastAPI server is running on port 8000")