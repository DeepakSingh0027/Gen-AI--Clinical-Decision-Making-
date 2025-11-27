import streamlit as st
import requests
import json

# --- CONFIGURATION ---
BACKEND_URL = "http://localhost:8000/chat/"

# --- MOCK DATA ---
PATIENT_DATA = {
    "name": "Rajesh Kumar",
    "id": "P-2025-001",
    "vitals": {"bp": "140/90", "hr": "78", "glucose": "180 mg/dL", "spo2": "98%"},
    "clinical_note": "Patient exhibits uncontrolled hyperglycemia (RBS: 180mg/dL). Recommendation: Intensify pharmacotherapy.",
    "patient_note": "Your blood sugar levels are higher than we'd like (180). We may need to adjust your medicine."
}

# --- PAGE SETUP ---
st.set_page_config(page_title="SAHYOG", page_icon="🧠", layout="wide")

# --- SIDEBAR (Role Selection) ---
with st.sidebar:
    st.title("🧠 SAHYOG")
    st.markdown("---")
    role = st.radio("Select View Mode:", ["Clinician 👨‍⚕️", "Patient 🙋‍♂️"])
    st.markdown("---")
    st.info("Backend Status: Connected to local API")

# --- HELPER: CHAT FUNCTION ---
def send_message(message, role_context):
    try:
        # We append context so the AI knows who it is talking to
        full_query = f"{role_context} {message}"
        response = requests.post(BACKEND_URL, json={"message": full_query})
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return "⚠️ Error: Backend returned an error."
    except Exception as e:
        return f"⚠️ Connection Error: Is the backend running? {e}"

# --- VIEW 1: CLINICIAN DASHBOARD ---
if role == "Clinician 👨‍⚕️":
    st.markdown("## 🏥 Clinical Decision Support")
    st.markdown(f"**Patient:** {PATIENT_DATA['name']} ({PATIENT_DATA['id']})")
    
    # Vitals Row
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Blood Pressure", PATIENT_DATA['vitals']['bp'])
    c2.metric("Heart Rate", PATIENT_DATA['vitals']['hr'])
    c3.metric("Glucose (RBS)", PATIENT_DATA['vitals']['glucose'], delta="-High", delta_color="inverse")
    c4.metric("SpO2", PATIENT_DATA['vitals']['spo2'])

    st.divider()

    col_info, col_chat = st.columns([1, 1])

    with col_info:
        st.subheader("📋 AI Clinical Summary")
        st.info(PATIENT_DATA['clinical_note'], icon="ℹ️")
        
        st.subheader("💊 Treatment Plan")
        st.checkbox("Increase Metformin to 1000mg")
        st.checkbox("Add Dapagliflozin 10mg")
        st.checkbox("Refer to Ophthalmologist")

    with col_chat:
        st.subheader("🤖 Clinical Co-Pilot")
        # Chat History Logic
        if "clinician_messages" not in st.session_state:
            st.session_state.clinician_messages = [{"role": "assistant", "content": "Ready for clinical queries."}]

        for msg in st.session_state.clinician_messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("Ask about guidelines or drug interactions..."):
            st.session_state.clinician_messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            with st.spinner("Analyzing..."):
                reply = send_message(prompt, "(Context: Answer technically for a doctor)")
                st.session_state.clinician_messages.append({"role": "assistant", "content": reply})
                st.chat_message("assistant").write(reply)

# --- VIEW 2: PATIENT DASHBOARD ---
else:
    st.markdown(f"## 👋 Hello, {PATIENT_DATA['name'].split()[0]}")
    st.success("You are in Patient Mode. Simplified views enabled.")

    col_main, col_bot = st.columns([3, 2])

    with col_main:
        st.subheader("🛡️ Doctor's Note (Simplified)")
        st.success(PATIENT_DATA['patient_note'], icon="🩺")

        st.subheader("✅ Your Action Items")
        st.markdown("- [ ] **Take medicine** with breakfast 💊")
        st.markdown("- [ ] **Drink water** (8 glasses) 💧")
        st.markdown("- [ ] **Walk** for 15 mins 🚶")

    with col_bot:
        st.subheader("💬 Health Assistant")
        # Chat History Logic
        if "patient_messages" not in st.session_state:
            st.session_state.patient_messages = [{"role": "assistant", "content": "Hi! Ask me anything about your health."}]

        for msg in st.session_state.patient_messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("Ask about side effects or diet..."):
            st.session_state.patient_messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            with st.spinner("Thinking..."):
                reply = send_message(prompt, "(Context: Answer simply for a patient)")
                st.session_state.patient_messages.append({"role": "assistant", "content": reply})
                st.chat_message("assistant").write(reply)