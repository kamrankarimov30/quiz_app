from quiz import Quiz
from user import User

def main():
    """
    quiz game main function
    """
    quiz = Quiz()

    users = []

    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty")
            continue
        user = User(name)

        num_questions = int(input(f"How many questions would you like to answer (1-{len(quiz.questions)})? "))
        while num_questions < 1 or num_questions > len(quiz.questions):
            print(f"Please select a valid number between 1 and {len(quiz.questions)}")
            num_questions = int(input(f"How many questions would you like to answer (1-{len(quiz.questions)})? "))

        quiz.ask_questions(num=num_questions)
        user.set_score(quiz.get_score())
        users.append(user)
    
       
        percentageScore = (user.get_score() / num_questions) * 100
        print(f"User {name}, your score: {user.get_score()}/{num_questions} ({percentageScore}%)")

        secondUser = input("Does someone else wanna take the quiz? (y/n)").strip().lower()
        if secondUser != "y" or secondUser != "yes":
            break
    
    highestScore = max(users, key=lambda i: i.get_score())
    print(f"Highest score: {highestScore.name} with a score of {highestScore.get_score()}")

    avg_score = sum([i.get_score() for i in users]) / len(users)
    print("\nResults:")
    for user in users:
        print(f"{user.name}'s score: {user.get_score()}")
    print(f"Avg score: {avg_score:.2f}")


if __name__ == "__main__":
    main()