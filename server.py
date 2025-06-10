# server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# --- Models ---

class NextRequest(BaseModel):
    history: List[str]
    choice: str

class NextResponse(BaseModel):
    narrative: str
    options: List[str]

class SessionBeat(BaseModel):
    narrative: str
    options: List[str]

class SessionResponse(BaseModel):
    session_id: str
    log: List[SessionBeat]

# --- Endpoints ---

@app.post("api/next", response_model=NextResponse)
async def next_beat(req: NextRequest):
    if not req.history or not req.choice:
        raise HTTPException(status_code=400, detail="Invalid request: history and choice are required.")
    
    # stubbed response
    return NextResponse(
        narrative="You step through the torchlit hallway and hear distant footsteps echoing.",
        options=[
            "Hide behind a pillar",
            "Call out to the guard",
            "Draw your sword and advance"
        ]
    )

@app.post("api/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str):
    # pretend only "demo" session exists
    if session_id != "demo":
        raise HTTPException(status_code=404, detail="Session not found.")
    
    return SessionResponse(
        id="demo",
        log=[
            SessionBeat(narrative="You stand at the castle gates...", options=["Knock", "Sneak around"]),
            SessionBeat(narrative="The guard raises and eyebrow...", options=["Charm him", "Attack"])   
        ]
    )

# --- Run the server ---
# uvicorn server:app --reload --port 3001