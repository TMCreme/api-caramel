"""
Helper functions
"""
# from database import schools

schools = []


def generate_school_id():
    school_length = len(schools)
    return school_length + 1


def school_update(schools, update_to_use):
    for school in schools:
        if school.get("id") == 1:
            school.update(update_to_use)
            return school
