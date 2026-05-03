
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("document_loaders/HR_Round_Cheat_Sheet.pdf")
docs = data.load()

splitter = TokenTextSplitter(
  chunk_size = 50,
  chunk_overlap = 5

)

chunks = splitter.split_documents(docs)

print(len(chunks))

# for i in chunks:
#   print(i.page_content)
#   print()


