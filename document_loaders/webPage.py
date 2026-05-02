from langchain_community.document_loaders import WebBaseLoader


url = "https://www.w3schools.com/django/django_models.php"

data = WebBaseLoader(url)
docs = data.load()

print(len(docs))
print(docs[0].page_content)