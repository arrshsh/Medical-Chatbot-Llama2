from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone as PineconeClient
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os 
load_dotenv()

PINECONE_API = os.getenv("PINECONE_API_KEY")  
PINECONE_ENV = os.getenv("PINECONE_API_ENV")

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone client
pc = PineconeClient(api_key=PINECONE_API)
index_name = "medical-chatbot"

# Create index if it doesn't exist
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=1536, metric="cosine")

docsearch = PineconeVectorStore.from_texts(
    texts=[t.page_content for t in text_chunks],
    embedding=embeddings,
    index_name=index_name  # Use index_name parameter instead of index
)