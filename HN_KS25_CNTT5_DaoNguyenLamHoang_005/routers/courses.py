from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models.course import Course
from models.course_category import CourseCategory
from schemas.course import CourseCreate, CourseResponse

router = APIRouter()

@router.post("/courses", response_model=None)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    category = db.query(CourseCategory).filter(CourseCategory.id == course.course_category_id).first()
    if category is None:
        return JSONResponse(
            status_code=404,
            content={
                "statusCode": 404,
                "error": "Not Found",
                "message": "Danh mục khóa học không tồn tại",
                "data": None
            }
        )
    existing_course = db.query(Course).filter(Course.course_code == course.course_code).first()
    if existing_course:
        return JSONResponse(
            status_code=400,
            content={
                "statusCode": 400,
                "error": "Bad Request",
                "message": "Mã khóa học đã tồn tại",
                "data": None
            }
        )
    new_course = Course(
        course_code=course.course_code,
        tuition_fee=course.tuition_fee,
        course_category_id=course.course_category_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    course_data = CourseResponse.model_validate(new_course)
    return JSONResponse(
        status_code=201,
        content={
            "statusCode": 201,
            "error": None,
            "message": "Thêm khóa học thành công",
            "data": course_data.model_dump()
        }
    )

@router.get("/courses", response_model=None)
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    result = []
    for course in courses:
        course_data = CourseResponse.model_validate(course)
        result.append(course_data.model_dump())
    return {
        "statusCode": 200,
        "error": None,
        "message": "Lấy danh sách khóa học thành công",
        "data": result
    }