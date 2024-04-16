"""
API Routes
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api_models import School, SchoolUpdate
from utils import school_update
from database import get_db, School as School_DB


schools = []
api_router = APIRouter(prefix="/api")


@api_router.get("/schools", response_model=list[School])
def get_schools(db: Session = Depends(get_db)):
    all_schools = db.query(School_DB).all()
    return all_schools


@api_router.get("/schools/{id}")
def get_school(id: int, db: Session = Depends(get_db)):
    # for school in schools:
    #     if school["id"] == id:
    #         return school
    school = [school for school in schools if school["id"] == id]
    return school


@api_router.post("/schools", response_model=School)
def create_school(school: School, db: Session = Depends(get_db)):
    new_school = School_DB(**dict(school))
    db.add(new_school)
    db.commit()
    db.refresh(new_school)
    return new_school


@api_router.put("/schools/{id}")
def update_school(id: int, school: SchoolUpdate):
    new_object = {
        "name": school.name,
        "location": school.location
    }
    school_obj = {k: v for k, v in new_object.items() if v is not None}
    obj = school_update(schools, school_obj)
    return obj


@api_router.delete("/schools/{id}")
def delete_school(id: int):
    for school in schools:
        if school['id'] == id:
            schools.remove(school)
            break

    return None
