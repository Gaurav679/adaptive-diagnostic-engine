
# AI Adaptive Diagnostic Engine

This project implements an adaptive testing system using FastAPI and MongoDB.

## Features
- Adaptive difficulty questions
- Ability score update using IRT-inspired algorithm
- MongoDB question storage
- AI-generated personalized study plan

## Tech Stack
- Python
- FastAPI
- MongoDB
- OpenAI API

## API Endpoints

POST /start-test  
Starts a new test session.

POST /submit-answer  
Submits an answer and returns the next adaptive question.

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
