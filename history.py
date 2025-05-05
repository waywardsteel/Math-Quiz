quiz_history.append({
            "number": question_number,
            "question": question,
            "correct_answer": correct_answer,
            "user_answer": user_answer,
            "result": result
        })

# Summary
print("\nMath quiz Completed!")
percentage = (score / question_number) * 100
print(f"You got {score} out of {question_number} correct. ({percentage:.1f}%)")

# Option to see history
show_history = input("\nWould you like to see your quiz history? (yes/no): ").strip().lower()
if show_history == "yes":
    print("\nQuiz History:")
    for item in quiz_history:
        print(f"Q{item['number']}: {item['question']}")
        if item['result'] == "Correct":
            print(f"✅✅✅ Correct! Your answer: {item['user_answer']}\n✅✅✅")
        else:
            print(f"❌❌❌ Incorrect. Your answer: {item['user_answer']}, Correct answer: {item['correct_answer']}\n❌❌❌")
