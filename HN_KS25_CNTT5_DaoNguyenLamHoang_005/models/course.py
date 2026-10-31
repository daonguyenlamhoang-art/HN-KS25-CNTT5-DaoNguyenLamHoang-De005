from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_code = Column(String(10), unique=True, nullable=False)
    tuition_fee = Column(Float, nullable=False)
    course_category_id = Column(
        Integer,
        ForeignKey("course_categories.id"),
        nullable=False
    )
    course_category = relationship(
        "CourseCategory",
        back_populates="courses"
    ) 