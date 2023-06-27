from dotenv import load_dotenv
import os
import openai
import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# import pdb; pdb.set_trace()

class WhisperExporter:

    def __init__(self):
        self._textes = []

    def whisper_to_text(self, path: str, filename: str):
        f = open(f".{path}", "rb")
        transcript = openai.Audio.transcribe("whisper-1", file=f)
        self.textes.append({"filename": filename, "text": transcript["text"]})
        return f"transcribed {path}"

    @staticmethod
    def to_txt(text_list: list):
        for text in text_list:
            with open(f"./text_files/{text['filename']}.txt", "w") as f:
                f.write("".join(text['text']))
                f.close()
                print(f"saved to text_files/{text['filename']}")

    @property
    def textes(self):
        return self._textes



if __name__ == "__main__":
    exporter = WhisperExporter()
    # loop over all files if they end with the allowed endings
    for file in [f for f in os.listdir("./audio_files") if os.path.splitext(f)[1] in [".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".wav", ".webm"]]:
        exporter.whisper_to_text(f"/audio_files/{file}", os.path.splitext(file)[0])
    exporter.to_txt(exporter.textes)
