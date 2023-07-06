# OpenAI Chatbot over your Audio files (supports Whatsapp audios)
This repository contains code and resources for demonstrating the power of OpenAI's Whisper API in combination with ChromaDB and LangChain for asking questions about your audio data. 
The demo showcases how to transcribe audio data into natural language with the Whisper API. The project also demonstrates how to vectorize data in chunks and get embeddings using OpenAI embeddings model.

We then use [LangChain](https://github.com/hwchase17/langchain) to ask questions based on our data which is vectorized using OpenAI embeddings model. 
We used [ChromaDB](https://github.com/chroma-core/chroma) database for storing and querying vectorized data.

## Getting Started
To get started with the demo, you will need to have Python (I use Python 3.8) installed on your machine.

1. Clone this repo
2. Install the required Python packages by running the following command:
`pip install -r requirements.txt`
3. You may need to run this if you get any errors related to the package
`brew install ffmpeg`
4. Set your `OPENAI_API_KEY` on `.env` file
5. Put your audio files in the `/audio_files` folder. It supports audios downladed from whatsapp web.
6. Run `python whisper.py` file to generate a .txt file out for each of your audio data
7. In line 51 of `ask_the_audio.py` change `text_files/sample.txt` for the name of the file you'd like to chat about
8. Now you can run `python ask_the_audio.py` which will start a chat bot that can answer questions over the .txt file.
