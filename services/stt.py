from google.cloud import speech
import io

def detect_language_from_audio_multi_pass(audio_path, possible_languages=None):
    if possible_languages is None:
        possible_languages = [
            "hi-IN",  # Hindi (India)
            "bn-IN",  # Bengali (India)
            "gu-IN",  # Gujarati (India)
            "kn-IN",  # Kannada (India)
            "ml-IN",  # Malayalam (India)
            "mr-IN",  # Marathi (India)
            "or-IN",  # Oriya (India)
            "pa-IN",  # Punjabi (India)
            "ta-IN",  # Tamil (India)
            "te-IN",  # Telugu (India)
            "ur-IN",  # Urdu (India)
        ]

    client = speech.SpeechClient()

    # Read audio once
    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    best_transcript = None
    best_detected_language = None
    highest_confidence = -1.0 # Confidence scores are between 0.0 and 1.0

    # print(f"Attempting to detect language from: {audio_path}")

    # Iterate through each possible language as the primary one
    for lang_code in possible_languages:
        # print(f"  Trying with primary language_code: {lang_code}")
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000, # IMPORTANT: Ensure this matches your audio
            language_code=lang_code,
            enable_automatic_punctuation=True
        )

        try:
            response = client.recognize(config=config, audio=audio)

            if not response.results:
                print(f"    No speech detected for {lang_code}.")
                continue # Skip to next language

            result = response.results[0]
            current_transcript = result.alternatives[0].transcript
            current_confidence = result.alternatives[0].confidence


            api_detected_language = result.language_code if hasattr(result, 'language_code') else lang_code

            # print(f"    Result for {lang_code}: Transcript='{current_transcript}', Confidence={current_confidence:.2f}, API Detected (if different): {api_detected_language}")

            if current_confidence > highest_confidence:
                highest_confidence = current_confidence
                best_transcript = current_transcript
                best_detected_language = lang_code # The language that yielded the highest confidence

        except Exception as e:
            print(f"    Error processing with language {lang_code}: {e}")

    if best_transcript:
        # print(f"\nFINAL DETECTION: Language: {best_detected_language}, Transcript: '{best_transcript}', Confidence: {highest_confidence:.2f}")
        return best_transcript, best_detected_language
    else:
        # print("\nCould not detect language for the provided audio.")
        return None, None