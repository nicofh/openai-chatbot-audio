# OpenAI Whisper API ChromaDB and LangChain Demo
This repository contains code and resources for demonstrating the power of OpenAI's Whisper API in combination with ChromaDB and LangChain for asking questions about your audio data. 
The demo showcases how to transcribe audio data into natural language with the Whisper API. The project also demonstrates how to vectorize data in chunks and get embeddings using OpenAI embeddings model.

We then use [LangChain](https://github.com/hwchase17/langchain) to ask questions based on our data which is vectorized using OpenAI embeddings model. 
We used [ChromaDB](https://github.com/chroma-core/chroma) database for storing and querying vectorized data.

## Getting Started
To get started with the demo, you will need to have Python (I use Python 3.8) installed on your machine. You will also need to install the required Python packages by running the following command:
`pip install -r requirements.txt`

You may need to run if you get any errors related to that package
`brew install ffmpeg`

All the `(m4a, mp3, mp4, mpeg, mpga, wav, webm, ogg)` files need to be in the `/audio_files` folder.

 **Run the `whisper.py` file to generate a .txt file out for each of your audio data**

Now you can run `ask_the_audio.py` which will start a chat bot that can answer questions over the .txt file.
