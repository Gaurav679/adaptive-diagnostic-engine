from pymongo import MongoClient
import os

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)

db = client["adaptive_test"]
questions_collection = db["questions"]
session_collection = db["sessions"]