from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

data = TextLoader("document_loaders/notes.txt")

docs = data.load()

splitter = CharacterTextSplitter(
  separator="",
  chunk_size = 10,
  chunk_overlap = 1
)

chunks = splitter.split_documents(docs)
print(len(chunks))
for i in chunks:
  print(i)
  print()