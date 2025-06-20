

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import traceback

# DB setup
from database.session import SessionLocal, engine
from models.student import Base
from crud.student_crud import save_profile

# AI Agents
from agents.skill_extractor import extract_skills
from agents.aptitude_mapper import map_aptitudes
from agents.role_retreiver import retrieve_roles
from agents.transition_planner import plan_transition
from agents.mentor_connector import connect_mentor

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Career Profile Analyzer",
    description="Analyze resumes with AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Career Profile Analyzer"}

@app.post("/process-profile")
async def process_profile(
    resume: UploadFile = File(...),
    github: str = Form(...),
    linkedin: str = Form(...),
    quiz: str = Form("")
):
    try:
        logger.info(f"Received resume: {resume.filename}")
        content = await resume.read()

        if len(content) > 10 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File too large")

        resume.file.seek(0) 

        skills = await extract_skills(resume, github, linkedin)
        aptitudes = await map_aptitudes(quiz, github)
        roles = await retrieve_roles(skills, aptitudes)
        roadmap = await plan_transition(roles, skills)
        mentors = await connect_mentor(roles)

        db = SessionLocal()
        save_profile(
            db, github, linkedin, quiz,
            skills, aptitudes, roles, roadmap, mentors
        )
        db.close()

        return JSONResponse(content={
            "skills": skills,
            "aptitudes": aptitudes,
            "roles": roles,
            "roadmap": roadmap,
            "mentors": mentors,
        })

    except Exception as e:
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
