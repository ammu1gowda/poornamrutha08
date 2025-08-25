# quiz_game.py

# List of questions as dictionaries
questions = [
    {
        "question": "Which of the following is a supervised learning algorithm?",
        "options": ["A.K-Means Clustering", "B. Decision Tree", "C. PCA", "D. DBSCAN"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for AI/ML?",
        "options": ["A. Python", "B. Java", "C. C++", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo", "D. Tesla"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Earth", "C. Jupiter", "D. Mars"],
        "answer": "D"
    }
]

# Function to run the quiz
def run_quiz():
    print("🎯 Welcome to the Quiz Game!")
    print("Choose the correct option (A, B, C, or D):\n")

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer: ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print("🎉 Quiz Finished!")
    print(f"Your Score: {score}/{len(questions)}")
    print("Thanks for playing!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
