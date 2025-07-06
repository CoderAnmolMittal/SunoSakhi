from google.cloud import texttospeech

def text_to_speech(
    text: str,
    language_code: str,
    output_filepath: str = "files/output/output.mp3"
) -> str:

    # Initialize the Google Cloud Text-to-Speech client
    client = texttospeech.TextToSpeechClient()

    # Set the text input
    synthesis_input = texttospeech.SynthesisInput(text=text)

    #get voice name
    voices = {
        "hi-IN": "hi-IN-Chirp3-HD-Autonoe",  # Hindi Chirp3 HD
        "bn-IN": "bn-IN-Chirp3-HD-Autonoe",  # Bengali (India) Chirp3 HD
        "gu-IN": "gu-IN-Chirp3-HD-Autonoe",  # Gujarati (India) Chirp3 HD
        "kn-IN": "kn-IN-Chirp3-HD-Autonoe",  # Kannada (India) Chirp3 HD
        "ml-IN": "ml-IN-Chirp3-HD-Autonoe",  # Malayalam (India) Chirp3 HD
        "mr-IN": "mr-IN-Chirp3-HD-Autonoe",  # Marathi (India) Chirp3 HD
        "or-IN": "or-IN-Chirp3-HD-Autonoe",  # Oriya (India)
        "pa-IN": "pa-IN-Chirp3-HD-Autonoe",  # Punjabi (India)
        "ta-IN": "ta-IN-Chirp3-HD-Autonoe",  # Tamil (India)
        "te-IN": "te-IN-Chirp3-HD-Autonoe",  # Telugu (India)
        "ur-IN": "ur-IN-Chirp3-HD-Autonoe",  # Urdu (India)
    }
    voice_name = voices.get(language_code)

    # Configure the voice parameters
    voice_params = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name,
    )

    # Configure the audio output format for MP3
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
    )

    try:
        # Perform the text-to-speech synthesis
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice_params,
            audio_config=audio_config
        )

        # Write the audio content to the specified file
        with open(output_filepath, "wb") as out:
            out.write(response.audio_content)
        return output_filepath

    except Exception as e:
        print(f"An error occurred during TTS: {e}")
        return f"Error: {e}"