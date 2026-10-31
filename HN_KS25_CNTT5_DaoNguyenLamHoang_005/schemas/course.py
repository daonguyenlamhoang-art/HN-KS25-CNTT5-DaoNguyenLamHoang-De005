from pydantic import BaseModel, Field, ConfigDict

class CourseCreate(BaseModel):
    course_code: str = Field(..., min_length=4, max_length=10)
    tuition_fee: float = Field(..., gt=0)
    course_category_id: int

class CourseCategoryResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class CourseResponse(BaseModel):
    id: int
    course_code: str
    tuition_fee: float
    course_category: CourseCategoryResponse
    model_config = ConfigDict(from_attributes=True)