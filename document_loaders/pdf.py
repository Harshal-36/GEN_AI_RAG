
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document_loaders/HR_Round_Cheat_Sheet.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
  chunk_size = 50,
  chunk_overlap = 10

)

chunks = splitter.split_documents(docs)

print(len(chunks))
print(chunks[0].page_content)
print(chunks[1].page_content)

# for i in chunks:
#   print(i.page_content)
#   print()


