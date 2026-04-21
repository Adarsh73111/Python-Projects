import PyPDF2
from gtts import gTTS
import os


def pdf_to_audiobook(pdf_path, audio_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""

            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    full_text += extracted

            clean_text = full_text.replace('\n', ' ')

            if clean_text.strip():
                print("Extracting text and calling TTS API...")
                tts = gTTS(text=clean_text, lang='en', slow=False)
                tts.save(audio_path)
                print(f"Success! Audiobook saved as {audio_path}")
            else:
                print("No readable text could be extracted from this PDF.")

    except FileNotFoundError:
        print(f"Error: Could not find '{pdf_path}'. Please ensure it is in the same folder.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    target_pdf = "sample.pdf"
    output_audio = "audiobook.mp3"
    pdf_to_audiobook(target_pdf, output_audio)