# 🤖 Digital Twin

An AI-powered digital twin that represents me on my website. Visitors can ask about my career, background, skills, and experience, and get answers grounded in my LinkedIn profile and personal summary.

## ✨ Features

- **Grounded answers:** responses are built from my LinkedIn PDF and a personal summary, so the twin doesn't invent details.
- **Stays on topic:** only handles professional questions and steers everything else back.
- **Lead capture:** if a visitor wants to get in touch, the twin collects their email and sends me a push notification.
- **Unknown-question logging:** anything it can't answer is recorded and sent to me, so I can improve its knowledge.
- **Clean chat UI:** custom-styled Gradio interface with example prompts.

## 🧱 Tech Stack

- **Python** and **Gradio** for the chat interface
- **Anthropic Claude (Haiku 4.5)** via the OpenAI-compatible SDK
- **Tool calling** for `record_user_details` and `record_unknown_question`
- **Pushover** for real-time notifications
- **pypdf** for parsing the LinkedIn profile

## 📁 Project Structure

```
├── app.py          # Gradio app and chat loop with tool handling
├── context.py      # System prompt built from LinkedIn PDF + summary
├── tools.py        # Tool definitions and Pushover notifications
├── styles.py       # CSS, JS, and example prompts
├── requirements.txt
└── .env.example
```

## 🚀 Getting Started

1. **Clone the repo**
```bash
   git clone https://github.com/<your-username>/digital-twin.git
   cd digital-twin
```
2. **Install dependencies**
```bash
   pip install -r requirements.txt
```
3. **Add your own data**
   - Put your LinkedIn export in `linkedin.pdf`
   - Write a short bio in `summary.txt`
4. **Configure environment variables**: copy `.env.example` to `.env` and fill in:
```
   ANTHROPIC_API_KEY=your_key
   PUSHOVER_USER=your_pushover_user_key
   PUSHOVER_TOKEN=your_pushover_app_token
```
5. **Run**
```bash
   python app.py
```

## 🔐 Security Notes

API keys are loaded from environment variables and never committed. All model and notification calls run server-side.

## 📄 License

MIT