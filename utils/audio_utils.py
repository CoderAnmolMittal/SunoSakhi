import os
from pathlib import Path

def convert_to_wav_16khz_mono(input_file_path):

    try:
        import librosa
        import soundfile as sf
    except ImportError:
        raise ImportError("librosa and soundfile are required. Install with: pip install librosa soundfile")

    # Check if input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")

    # Generate output file path
    input_path = Path(input_file_path)
    output_file_path = str(input_path.parent / "input.wav")

    try:
        # Load audio file (automatically converts to mono and resamples to 16kHz)
        audio_data, _ = librosa.load(input_file_path, sr=16000, mono=True)

        # Save as WAV file
        sf.write(output_file_path, audio_data, 16000)

        # Delete original file after successful conversion (only if different from output)
        if os.path.abspath(input_file_path) != os.path.abspath(output_file_path):
            os.remove(input_file_path)

        return output_file_path

    except Exception as e:
        raise Exception(f"Conversion error: {str(e)}")