# Gemini LLM Applications: Text, Image, and Chat History

Welcome to the **Gemini LLM Applications** repository! This project demonstrates three innovative applications of the Gemini LLM (Large Language Model) for text-based question-answering, image-based analysis, and interactive chat history preservation. Built with **Streamlit**, these applications provide seamless integration with the Gemini API for dynamic and intelligent user interactions.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Text-Based Q&A Application](#text-based-q&a-application)
  - [Image-Based Analysis Application](#image-based-analysis-application)
  - [Chat History Preservation Application](#chat-history-preservation-application)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

---

## Project Overview
This repository contains three unique applications that showcase the capabilities of the Gemini LLM in various contexts:
1. **Text-Based Q&A**: Provides instant responses to user questions using natural language understanding.
2. **Image-Based Analysis**: Analyzes uploaded images and generates insights based on the image content and user-provided prompts.
3. **Chat History Preservation**: Maintains an interactive chat session with preserved history, enabling users to track their queries and responses seamlessly.

---

## Features
### 1. Text-Based Q&A Application
- Enter a query and receive instant, accurate answers.
- Powered by the Gemini LLM for robust text comprehension.

### 2. Image-Based Analysis Application
- Upload an image (JPG, JPEG, PNG) and get detailed insights.
- Combines text prompts with image analysis for enhanced responses.

### 3. Chat History Preservation Application
- Engage in a conversational experience with the Gemini LLM.
- Retain and display chat history for user convenience.

---

## Installation
To run the applications locally, follow these steps:

1. Create an API_KEY Update your API Key on ".env" file.
2. Create a virtual environment
3. Install dependencies: 
    "pip install -r requirements.txt"
4. Set up the environment variables:
    - Create a .env file in the root directory.
    - Add your Google Gemini API key:
        "GOOGLE_API_KEY=your_api_key_here"
5. Run the desired application:
    - streamlit run app_text_based.py  # For Text-Based Q&A
    - streamlit run app_image_based.py  # For Image-Based Analysis
    - streamlit run app_chat_history.py  # For Chat History Preservation

## Usage

### Text-Based Q&A Application
1. Launch the app.
2. Enter a question in the text input box.
3. Click the **"Ask the Question"** button to get an instant response.

### Image-Based Analysis Application
1. Launch the app.
2. Upload an image (JPG, JPEG, PNG) using the file uploader.
3. Optionally, enter a text prompt for additional context.
4. Click **"Tell about the image"** to generate a response.

### Chat History Preservation Application
1. Launch the app.
2. Enter a query in the text input box.
3. Click **"Ask the question"** to interact with the Gemini LLM.
4. View the entire chat history displayed at the bottom of the page.

---

## Technologies Used
- **Python**: Core programming language for development.
- **Streamlit**: Framework for building web applications.
- **Google Generative AI**: Gemini LLM API for natural language and image understanding.
- **Pillow**: Library for image processing.
- **dotenv**: For managing environment variables securely.

---

## Future Enhancements
- Support for multiple languages in the text-based Q&A application.
- Advanced image analysis with multimodal understanding.
- Options to download chat history in formats like PDF or JSON.
- User authentication for personalized experiences.

---


### Contact
For questions or feedback, reach out at:
- Replace `Ktrimalrao` and `trimalrao2004@gmail.com` and `www.linkedin.com/in/k-trimal-rao-397924253`
- Add any specific branding, images, or details unique to your project.
