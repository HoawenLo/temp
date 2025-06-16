from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Dummy RAG LLM function — replace with actual logic
def rag_llm_chat(query: str) -> str:
    return f"You said: '{query}'. Here's an intelligent answer from the RAG system."

app = FastAPI()

# Serve static HTML
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/chat")
async def chat(req: ChatRequest):
    response = rag_llm_chat(req.message)
    return {"response": response}
