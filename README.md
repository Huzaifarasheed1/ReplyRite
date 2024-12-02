# ReplyRite 💬

## Overview
ReplyRite is a conversational AI application built using Streamlit and Google's Gemini Pro, offering an interactive chatting experience with streaming responses.

## Features
- Real-time chat interface
- Streaming responses from Gemini Pro
- Persistent chat history
- Simple and intuitive user experience

## Prerequisites
- Python 3.8+
- Streamlit
- Google's Generative AI Library
- Active Google AI API Key

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Huzaifarasheed1/replyrite.git
cd replyrite
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your_google_generative_ai_api_key
```

## Running the Application
```bash
streamlit run bot.py
```

## Project Structure
```
replyrite/
│
├── bot.py           # Main Streamlit application
├── .env             # Environment variables (not tracked in git)
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

## Environment Variables
- `GOOGLE_API_KEY`: Your Google Generative AI API key for authentication

## Key Components
- Streamlit for UI
- Google's Generative AI for conversational responses
- Session state management
- Streaming response handling

## Customization
- Modify the model in `get_chat_session()` to use different Gemini versions
- Adjust UI elements in Streamlit configuration
- Customize chat history display

## Troubleshooting
- Ensure API key is valid and has necessary permissions
- Check internet connectivity
- Verify all dependencies are installed

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

