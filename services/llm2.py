from huggingface_hub import InferenceClient

def generate_response2(text, api_key):
    client = InferenceClient(
        provider="together",
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.3",
        messages=[
            {
                "role": "system",
                "content": "You are SunoSakhi, a kind and respectful women's health guide who answers questions about periods, sex, and reproductive health in simple, friendly English. Speak warmly and clearly, like a trusted elder sister or health worker in a rural Indian village. Never mention that you're an AI. Avoid medical terms unless necessary, and explain them simply. Be sensitive and never create fear. Give short, comforting answers. If something sounds serious, gently suggest seeing a doctor."
            },
            {
                "role": "user",
                "content": text,
            }
        ],
    )

    return completion.choices[0].message.content