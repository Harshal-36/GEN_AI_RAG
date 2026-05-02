from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader , PyPDFLoader, WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

model = ChatMistralAI(model = "mistral-small-2603")

#data = TextLoader("document_loaders/notes.txt")
#data = PyPDFLoader("document_loaders/HR_Round_Cheat_sheet.pdf")

url = "https://www.w3schools.com/django/django_models.php"
data = WebBaseLoader(url)
docs = data.load()

question = input("what you want to ask: ")

template = ChatPromptTemplate.from_messages([
  ("system", "you are an ai that summarizes the text"),
  ("human", """
   
   Data:
   {data}

   question:
   {question}
   """)
])

prompt = template.format_messages(data = docs[0].page_content, question = question)


result = model.invoke(prompt)
print(result.content)