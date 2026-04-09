import pdfplumber
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect to ChromaDB
client = chromadb.PersistentClient(path="../chroma_db")
collection = client.get_or_create_collection(name="documents")

def extract_text(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def chunk_text(text: str, chunk_size=500, overlap=50) -> list:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def process_pdf(file_path: str, filename: str):
    print(f"Processing {filename}...")
    
    # Step 1: Extract text
    text = extract_text(file_path)
    
    # Step 2: Chunk text
    chunks = chunk_text(text)
    
    # Step 3: Embed and store in ChromaDB
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{filename}_chunk_{i}"]
        )
    
    print(f"Done! Stored {len(chunks)} chunks.")
    return len(chunks)