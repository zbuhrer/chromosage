from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_chat_response(chat_history, model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF", temperature=0.7):
    response = client.chat.completions.create(
        model=model,
        messages=chat_history,
        temperature=temperature,
    )
    return response.choices[0].message.content