from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from typing import List
from langchain.schema import Document
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Genie:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.loader = TextLoader(self.file_path)
        self.documents = self.loader.load()
        self.texts = self.text_split(self.documents)
        self.vectordb = self.embeddings(self.texts)
        self.genie = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=self.vectordb.as_retriever(search_kwargs={"k": 1}))

    @staticmethod
    def text_split(documents: TextLoader):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        return texts

    @staticmethod
    def embeddings(texts: List[Document]):
        embeddings = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(texts, embeddings)
        return vectordb

    def ask(self, query: str):
        return self.genie.run(query)


if __name__ == "__main__":
    genie = Genie("text_files/virAudio.txt")
    # print(genie.ask("Give me a list of questions that this person wants to know. Reply in original language"))
    # print(genie.ask("Give me a summary of this text in bullet points. Reply in original language. Sender name is 'Vir'. I'm 'Gordy'"))
    print(genie.ask("This is an audio I received. Tell me what is it about. Reply in original language"))