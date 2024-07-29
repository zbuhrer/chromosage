# ./chat_model.py
from openai import OpenAI


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_chat_response(
        chat_history, 
        model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF", 
        temperature=0.7, 
        max_tokens=1000,
        ):
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=chat_history,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function to handle chat interactions
def chat_interface(query):
    chat_history = [{"role": "user", "content": query}]
    response = get_chat_response(chat_history)
    chat_history.append({"role": "assistant", "content": response})
    return response

if __name__ == "__main__":
    query = "What can you tell me about ChromoSage?"
    print(chat_interface(query))