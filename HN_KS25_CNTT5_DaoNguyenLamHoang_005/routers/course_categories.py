from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from models.course import Course
from models.course_category import CourseCategory

router = APIRouter()

@router.delete("/course-categories/{id}")
def delete_course_category(id: int, db: Session = Depends(get_db)):
    category = db.query(CourseCategory).filter(CourseCategory.id == id).first()
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

    course = db.query(Course).filter(Course.course_category_id == id).first()
    if course:
        return JSONResponse(
            status_code=400,
            content={
                "statusCode": 400,
                "error": "Bad Request",
                "message": "Không thể xóa danh mục đang có khóa học",
                "data": None
            }
        )

    db.delete(category)
    db.commit()
    return {
        "statusCode": 200,
        "error": None,
        "message": "Xóa danh mục khóa học thành công",
        "data": None
    }