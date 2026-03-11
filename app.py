from fastapi import FastAPI
from database import questions_collection, session_collection
from adaptive_engine import update_ability
from models import AnswerRequest
import uuid
app = FastAPI()

@app.post("/start-test")
def start_test():

    session_id = str(uuid.uuid4())

    session_collection.insert_one({
        "session_id": session_id,
        "ability": 0.5,
        "answered": []
    })

    question = questions_collection.find_one({"difficulty": {"$gte":0.4,"$lte":0.6}})

    if question:
        question["_id"] = str(question["_id"])

    return {
        "session_id": session_id,
        "question": question
    }
@app.post("/submit-answer")
def submit_answer(req: AnswerRequest):

    session = session_collection.find_one({"session_id": req.session_id})

    question = questions_collection.find_one({"_id": req.question_id})

    correct = question["correct_answer"] == req.answer

    ability = update_ability(session["ability"], correct)

    session_collection.update_one(
        {"session_id": req.session_id},
        {"$set":{"ability":ability}}
    )

    next_question = questions_collection.find_one({
        "difficulty":{"$gte": ability-0.1,"$lte": ability+0.1}
    })

    return {
        "correct": correct,
        "next_question": next_question
    }