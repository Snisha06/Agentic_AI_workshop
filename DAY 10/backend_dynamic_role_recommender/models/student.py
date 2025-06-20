from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database.session import Base

class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)
    github = Column(String)
    linkedin = Column(String)
    quiz = Column(Text)
    skills = Column(Text)        # JSON string
    aptitudes = Column(Text)     # JSON string
    roles = Column(Text)
    roadmap = Column(Text)
    mentors = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
