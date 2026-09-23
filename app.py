from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import os



load_dotenv(override=True)

pushover_url = "https://api.pushover.net/1/messages.json"

anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set")
    
MODEL = "claude-haiku-4-5-20251001"
anthropic_url = "https://api.anthropic.com/v1/"
anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url) 



system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system + history + [{"role": "user", "content": message}]
    response = anthropic.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = anthropic.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(
            show_label=False,
            type="messages"
        ),
        type="messages",
        css=CSS,
        js=JS,
        theme=gr.themes.Base()
    ).launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 7860)))
