# Step 1: Install Required Libraries
!pip install openai --quiet

# Step 2: Import Required Libraries
import openai
import os

# Step 3: Set Your OpenAI API Key
openai.api_key = "your-api-key-here"  # Replace with your actual key

# Step 4: Define the Chatbot Function
def customer_support_bot(prompt, chat_history=[]):
    messages = [{"role": "system", "content": "You are a helpful customer support assistant."}]
    for user_input, bot_reply in chat_history:
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "assistant", "content": bot_reply})
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if enabled
        messages=messages,
        temperature=0.5,
        max_tokens=200
    )

    reply = response.choices[0].message['content']
    return reply

# Step 5: Simulate a Conversation
chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    reply = customer_support_bot(user_input, chat_history)
    chat_history.append((user_input, reply))
    print("Bot:", reply)
