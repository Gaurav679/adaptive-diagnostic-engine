from pydantic import BaseModel

class AnswerRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str