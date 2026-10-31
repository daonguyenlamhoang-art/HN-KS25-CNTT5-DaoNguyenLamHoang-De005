from fastapi import FastAPI
from database import Base, engine
from models.course import Course
from models.course_category import CourseCategory
from routers import courses, course_categories

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(courses.router)
app.include_router(course_categories.router)