import re
raw_courses = [
    {"course_code": "K301","category": "programming","tuition_fee": 4500000,"status": "open"},
    {"course_code": " k101 ","category": "design","tuition_fee": 2800000,"status": "open"},
    {"course_code": "K202","category": "marketing","tuition_fee": 3200000,"status": "full"},
    {"course_code": "K102","category": "design","tuition_fee": 2500000,"status": "closed"},
    {"course_code": "K302","category": "programming","tuition_fee": 5200000,"status": "open"}
]

def clean_and_validate_courses(courses):
    result = []
    for course in courses:
        code = course["course_code"].strip().upper()
        if re.fullmatch(r"K[0-9]+", code):
            new_course = course.copy()
            new_course["course_code"] = code
            result.append(new_course)
    return result

def search_courses(courses, max_tuition_fee, status=None):
    result = []
    for course in courses:
        if course["tuition_fee"] <= max_tuition_fee:
            if status is None or course["status"] == status:
                result.append(course)
    return result

def sort_courses_by_tuition_fee_desc(courses):
    result = courses.copy()
    n = len(result)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if result[j]["tuition_fee"] < result[j + 1]["tuition_fee"]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result