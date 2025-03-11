# AI Automation & Reporting System

## Overview

The **AI Automation & Reporting System** is a Streamlit-based web application that allows users to interact with an AI system through multiple input methods. The system can process user queries through:

- **🎙️ Microphone Input** (Speech-to-Text conversion)
- **📤 Audio File Upload** (MP3, WAV transcription)
- **📸 Image Upload for OCR** (Extract text from images)
- **📝 Text Input** (Manual text entry)

Once the user query is processed, the system generates an **AI response** and provides an option to **download the response as a PDF report**.

## Features

✅ **Multi-Input Support:** Users can input queries using voice, text, or images.
✅ **Speech Recognition:** Converts audio to text for processing.
✅ **OCR Processing:** Extracts text from uploaded images.
✅ **AI-Powered Decision Making:** Uses backend AI models to analyze and respond to queries.
✅ **PDF Report Generation:** Automatically generates and downloads a report based on the AI's response.
✅ **User Personalization:** Allows users to enter their names for a personalized experience.

## Technologies Used

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** Python
- **Audio Processing:** Speech-to-Text (STT)
- **OCR Processing:** Optical Character Recognition (OCR)
- **PDF Generation:** Report generation from AI responses

## Installation & Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Virtual environment (optional but recommended)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shakeel401/ai-automation-reporting.git
   cd ai-automation-reporting
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # For macOS/Linux
   env\Scripts\activate  # For Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Select Input Method:** Choose from Microphone, Audio File, Image (OCR), or Text Input.
2. **Provide Input:** Record audio, upload a file, or enter text.
3. **Process Query:** Click the "🔍 Process Query" button to get an AI-generated response.
4. **Download PDF Report:** Click the "📥 Download Report (PDF)" button to save the response.

## Project Structure

```
├── backend/
│   ├── decision_making.py   # AI logic for processing queries
│   ├── stt_processor.py     # Speech-to-Text processing
│   ├── pdf_generator.py     # Generates PDF reports
│   ├── ocr_processor.py     # OCR text extraction
│
├── frontend/
│   ├── app.py               # Streamlit UI
│
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
```

## Contributing

Feel free to contribute by submitting issues or pull requests. Follow standard best practices for Python development.

---

**Happy Automating! 🚀**

