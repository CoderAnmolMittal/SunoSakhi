from google.cloud import translate_v2 as translate

def translate_text(text, source_language=None, target_language=None):

    try:
        # Initialize the Google Translate client
        translate_client = translate.Client()

        # Perform translation
        if source_language:
            translation = translate_client.translate(
                text,
                source_language=source_language,
                target_language=target_language
            )
        else:
            # Auto-detect source language
            translation = translate_client.translate(
                text,
                target_language=target_language
            )

        # Extract translated text
        translated_text = translation['translatedText']

        return translated_text

    except Exception as e:
        raise Exception(f"Translation failed: {str(e)}")
