import os
from dotenv import load_dotenv
from utils.audio_utils import convert_to_wav_16khz_mono
from services.stt import detect_language_from_audio_multi_pass
from services.translate import translate_text
# from services.llm import generate_response
from services.llm2 import generate_response2
from services.tts import text_to_speech

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("HF_TOKEN")

#start
audio_formats = ['.mp3', '.wav', '.m4a', '.flac', '.ogg', '.aac', '.wma']
audio_path = None

for format_ext in audio_formats:
    potential_path = f"files/input/upload{format_ext}"
    if os.path.exists(potential_path):
        audio_path = potential_path
        break

if audio_path is None:
    raise FileNotFoundError("No upload file found with supported audio formats")

converted_audio_path = convert_to_wav_16khz_mono(audio_path)
transcript, lang_code = detect_language_from_audio_multi_pass(converted_audio_path)
translated_text = translate_text(transcript, source_language=lang_code, target_language='en')
# response = generate_response(translated_text)
response = generate_response2(translated_text, api_key)
translated_response = translate_text(response, source_language='en', target_language=lang_code)
text_to_speech(translated_response, language_code=lang_code)


# for debugging
# print("Transcript:", transcript)
# print("Detected Language Code:", lang_code)
# print("Trans:", translated_text)
# print("response:", response)
# print("output", translated_response)
