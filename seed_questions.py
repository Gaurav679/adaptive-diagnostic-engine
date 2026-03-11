from database import questions_collection

questions = [

{
"question":"2 + 2 = ?",
"options":["1","2","3","4"],
"correct_answer":"4",
"difficulty":0.1,
"topic":"Arithmetic",
"tags":["addition"]
},

{
"question":"5 × 6 = ?",
"options":["25","30","35","40"],
"correct_answer":"30",
"difficulty":0.2,
"topic":"Arithmetic",
"tags":["multiplication"]
},

{
"question":"Solve: x + 3 = 7",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.3,
"topic":"Algebra",
"tags":["equation"]
},

{
"question":"Solve: 2x = 10",
"options":["2","3","5","6"],
"correct_answer":"5",
"difficulty":0.3,
"topic":"Algebra",
"tags":["linear"]
},

{
"question":"Solve: 2x + 4 = 12",
"options":["3","4","5","6"],
"correct_answer":"4",
"difficulty":0.4,
"topic":"Algebra",
"tags":["linear equation"]
},

{
"question":"15% of 200 = ?",
"options":["20","25","30","35"],
"correct_answer":"30",
"difficulty":0.4,
"topic":"Percentage",
"tags":["percent"]
},

{
"question":"25% of 80 = ?",
"options":["10","15","20","25"],
"correct_answer":"20",
"difficulty":0.4,
"topic":"Percentage",
"tags":["percent"]
},

{
"question":"Square root of 144?",
"options":["10","11","12","13"],
"correct_answer":"12",
"difficulty":0.5,
"topic":"Arithmetic",
"tags":["square root"]
},

{
"question":"10^2 = ?",
"options":["10","20","100","200"],
"correct_answer":"100",
"difficulty":0.5,
"topic":"Arithmetic",
"tags":["power"]
},

{
"question":"Derivative of x^2?",
"options":["x","2x","x^2","2"],
"correct_answer":"2x",
"difficulty":0.7,
"topic":"Calculus",
"tags":["derivative"]
},

{
"question":"Derivative of 3x?",
"options":["3","x","0","6"],
"correct_answer":"3",
"difficulty":0.6,
"topic":"Calculus",
"tags":["derivative"]
},

{
"question":"Area of square (side=5)?",
"options":["20","25","30","35"],
"correct_answer":"25",
"difficulty":0.3,
"topic":"Geometry",
"tags":["area"]
},

{
"question":"Perimeter of square (side=4)?",
"options":["12","14","16","18"],
"correct_answer":"16",
"difficulty":0.3,
"topic":"Geometry",
"tags":["perimeter"]
},

{
"question":"Probability of head in coin?",
"options":["0","0.25","0.5","1"],
"correct_answer":"0.5",
"difficulty":0.4,
"topic":"Probability",
"tags":["coin"]
},

{
"question":"Opposite of 'Happy'?",
"options":["Sad","Angry","Joy","Fun"],
"correct_answer":"Sad",
"difficulty":0.2,
"topic":"Vocabulary",
"tags":["antonym"]
},

{
"question":"Synonym of 'Big'?",
"options":["Large","Small","Tiny","Short"],
"correct_answer":"Large",
"difficulty":0.2,
"topic":"Vocabulary",
"tags":["synonym"]
},

{
"question":"3^3 = ?",
"options":["6","9","27","81"],
"correct_answer":"27",
"difficulty":0.5,
"topic":"Arithmetic",
"tags":["power"]
},

{
"question":"Mean of 2,4,6?",
"options":["3","4","5","6"],
"correct_answer":"4",
"difficulty":0.5,
"topic":"Statistics",
"tags":["mean"]
},

{
"question":"Median of 1,3,5?",
"options":["1","3","5","9"],
"correct_answer":"3",
"difficulty":0.5,
"topic":"Statistics",
"tags":["median"]
},

{
"question":"Limit of x→0 (sin x / x)?",
"options":["0","1","∞","-1"],
"correct_answer":"1",
"difficulty":0.9,
"topic":"Calculus",
"tags":["limit"]
}

]

questions_collection.insert_many(questions)

print("20 GRE questions inserted successfully")