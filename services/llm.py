from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("adi2606/Menstrual-Health-Awareness-Chatbot")
model = AutoModelForSeq2SeqLM.from_pretrained("adi2606/Menstrual-Health-Awareness-Chatbot")

# Function to generate a response from the chatbot
def generate_response(input_text):
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate the output (the response)
    outputs = model.generate(**inputs)

    # Decode the output back to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response