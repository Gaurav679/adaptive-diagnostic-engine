from fastapi import FastAPI
from database import questions_collection, session_collection
from adaptive_engine import update_ability
from models import AnswerRequest
from bson import ObjectId
import uuid

app = FastAPI()

@app.post("/start-test")
def start_test():

    session_id = str(uuid.uuid4())

    session_collection.insert_one({
        "session_id": session_id,
        "ability": 0.5,
        "answered":[]
    })

    question = questions_collection.find_one({"difficulty":{"$gte":0.4,"$lte":0.6}})

    if question:
        question["_id"] = str(question["_id"])

    return {
        "session_id": session_id,
        "question": question
    }

from bson import ObjectId

@app.post("/submit-answer")
def submit_answer(req: AnswerRequest):

    session = session_collection.find_one({"session_id": req.session_id})

    if not session:
        return {"error": "Session not found"}

    question = questions_collection.find_one({"_id": ObjectId(req.question_id)})

    if question is None:
        return {"error": "Question not found"}

    correct = question["correct_answer"] == req.answer

    new_ability = update_ability(
        session["ability"],
        question["difficulty"],
        correct
    )

    session_collection.update_one(
        {"session_id": req.session_id},
        {"$set": {"ability": new_ability}}
    )

    next_question = questions_collection.find_one({
        "difficulty": {
            "$gte": new_ability - 0.1,
            "$lte": new_ability + 0.1
        }
    })

    if next_question:
        next_question["_id"] = str(next_question["_id"])

    return {
        "correct": correct,
        "ability": new_ability,
        "next_question": next_question
    }