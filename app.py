import gradio as gr

# --- Simple Mental Health Chatbot ---
def chatbot(user_input):
    if not user_input.strip():
        return "Please type something 🙏"

    text = user_input.lower()

    if "sad" in text:
        return "I'm sorry you're feeling sad 💙. Talking to someone you trust might help."
    elif "tired" in text:
        return "It sounds like you’re tired. Try taking a short rest or drinking water."
    elif "nervous" in text or "anxious" in text:
        return "Feeling nervous is normal 🌱. Take a deep breath, you’re doing fine."
    elif "happy" in text:
        return "That’s wonderful! 🎉 Keep doing what makes you feel good."
    else:
        return "I hear you. Can you tell me a bit more about how you’re feeling?"

# --- Gradio Interface ---
iface = gr.Interface(
    fn=chatbot,
    inputs="text",
    outputs="text",
    title="🌱 Mental Health Chatbot",
    description="A simple AI chatbot for mental health support. \
    _(Not a substitute for professional help. If you are in crisis, please call your local emergency number.)_"
)

iface.launch()
