
from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader("document_loaders/HR_Round_Cheat_Sheet.pdf")
docs = data.load()

print(len(docs))


