from pydantic import BaseModel


class ReviewRequest(BaseModel):
    review: str


class ReviewResponse(BaseModel):
    review: str
    prediction: str