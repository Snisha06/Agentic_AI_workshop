from models.student import StudentProfile
from sqlalchemy.orm import Session
import json

def save_profile(db: Session, github, linkedin, quiz, skills, aptitudes, roles, roadmap, mentors):
    profile = StudentProfile(
        github=github,
        linkedin=linkedin,
        quiz=quiz,
        skills=json.dumps(skills),
        aptitudes=json.dumps(aptitudes),
        roles=json.dumps(roles),
        roadmap=json.dumps(roadmap),
        mentors=json.dumps(mentors)
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile
