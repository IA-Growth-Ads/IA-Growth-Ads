from fastapi import APIRouter

router = APIRouter()

@router.get("/ads/")
def get_ads():
    return [{"id": 1, "title": "Publicité 1"}, {"id": 2, "title": "Publicité 2"}]

@router.post("/ads/")
def create_ad(title: str):
    return {"message": f"Publicité '{title}' créée avec succès"}
