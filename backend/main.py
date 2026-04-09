from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

# Test route
@app.get("/")
def read_root():
    return {"message": "SupportBot API is running!"}

# Route 1: Upload a PDF
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "received"}

# Route 2: Chat endpoint
class ChatRequest(BaseModel):
    question: str
    session_id: str

@app.post("/chat")
async def chat(request: ChatRequest):
    return {"question": request.question, "answer": "placeholder answer"}