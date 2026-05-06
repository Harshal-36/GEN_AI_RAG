from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
load_dotenv()

data = PyPDFLoader("document_loaders/HR_Round_Cheat_Sheet.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
  chunk_size = 200,
  chunk_overlap = 40

)

chunks = splitter.split_documents(docs)

embedding_model = embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

vectorstore = Chroma.from_documents(
  documents=chunks,
  embedding=embedding_model,
  persist_directory="chroma_db"
)


