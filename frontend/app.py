import os
import streamlit as st
import tempfile
from streamlit_mic_recorder import mic_recorder
from backend.decision_making import process_query
from backend.stt_processor import transcribe_audio
from backend.pdf_generator import generate_pdf
from backend.ocr_processor import extract_text_from_image

# **Set Page Configurations**
st.set_page_config(page_title="AI Automation System", layout="wide")

# **Title**
st.title("🤖 AI Automation & Reporting System")

# **Personalization - User Settings**
st.sidebar.header("⚙️ Personalization Settings")
user_name = st.sidebar.text_input("Enter Your Name", value="User")
st.sidebar.write(f"👋 Welcome, {user_name}!")

# **User Input Selection**
st.subheader("🛠️ Select Input Method")
input_method = st.radio("Choose one input method:", ["Microphone", "Audio File", "Image (OCR)", "Text Input"])

user_input = None  # Initialize user input variable

# **🎙️ Microphone Input**
if input_method == "Microphone":
    st.subheader("🎙️ Record & Convert Speech to Text")
    audio_bytes = mic_recorder(start_prompt="Start Recording", stop_prompt="Stop Recording", key="recorder")

    if audio_bytes:
        if isinstance(audio_bytes, dict) and "bytes" in audio_bytes:
            audio_bytes = audio_bytes["bytes"]  # Extract actual audio bytes

        if isinstance(audio_bytes, bytes):  # Ensure it is in bytes format
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(audio_bytes)
                temp_audio_path = temp_audio.name

            user_input = transcribe_audio(temp_audio_path)
            os.remove(temp_audio_path)  # Cleanup
        else:
            st.error("❗ Invalid audio format received. Please try recording again.")

# **📤 Upload Audio File**
elif input_method == "Audio File":
    st.subheader("📤 Upload an Audio File (MP3, WAV)")
    audio_file = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])

    if audio_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio.write(audio_file.read())
            temp_audio_path = temp_audio.name

        user_input = transcribe_audio(temp_audio_path)
        os.remove(temp_audio_path)  # Cleanup

# **📸 Upload Image for OCR**
elif input_method == "Image (OCR)":
    st.subheader("📸 Upload an Image for OCR")
    image_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if image_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image:
            temp_image.write(image_file.read())
            temp_image_path = temp_image.name

        user_input = extract_text_from_image(temp_image_path)
        os.remove(temp_image_path)  # Cleanup

# **📝 Text Input**
elif input_method == "Text Input":
    st.subheader("📝 Enter Your Query")
    user_input = st.text_input("Type your query here...")

# **Process Input & Generate PDF**
if user_input and st.button("🔍 Process Query"):
    st.write("**Processing...**")
    ai_response = process_query(user_input)
    st.write("**🤖 AI Response:**", ai_response)
    
    # Generate PDF
    pdf_filename = generate_pdf(ai_response)
    with open(pdf_filename, "rb") as f:
        st.download_button("📥 Download Report (PDF)", f, file_name="report.pdf")
