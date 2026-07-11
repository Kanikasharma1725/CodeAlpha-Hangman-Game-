import random
from data.game_data import GAME_DATA
from src.graphics import HANGMAN_STAGES

def play_hangman():
    total_score = 0
    print("=" * 50)
    print("                HANGMAN GAME                ")
    print("=" * 50)

    while True:
        print("\n--- SELECT A CATEGORY ---")
        for key, value in GAME_DATA.items():
            category_name = value["category"]
            print(f"{key}. {category_name}")
        
        exit_number = len(GAME_DATA) + 1
        print(f"{exit_number}. Exit")
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == str(exit_number):
            print("\n" + "=" * 50)
            print(f"Thank you for playing! Total Score: {total_score}")
            print("=" * 50)
            break
            
        if choice in GAME_DATA:
            category_name = GAME_DATA[choice]["category"]
            word_list = GAME_DATA[choice]["items"]
            
            selected_item = random.choice(word_list)
            secret_word = selected_item["word"]
            word_hint = selected_item["hint"]
            
            guessed_letters = set()
            incorrect_guesses = 0
            max_attempts = 6
            
            print(f"\nCategory: {category_name.upper()}")
            print(f"Hint: {word_hint}")
            
            while incorrect_guesses < max_attempts:
                print(HANGMAN_STAGES[incorrect_guesses])
                
                display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
                print(f"\nWord: {' '.join(display_word)}")
                print(f"Attempts Remaining: {max_attempts - incorrect_guesses}")
                
                sorted_guesses = sorted(list(guessed_letters))
                print(f"Guessed Letters: {', '.join(sorted_guesses) if sorted_guesses else 'None'}")
                
                guess = input("\nGuess a letter: ").lower().strip()
                print("-" * 40)
                
                if len(guess) != 1 or not guess.isalpha():
                    print("Invalid input. Please enter a single alphabetical letter.")
                    continue
                    
                if guess in guessed_letters:
                    print(f"You already guessed {guess}. Try another letter.")
                    continue
                    
                guessed_letters.add(guess)
                
                if guess in secret_word:
                    print(f"Correct! {guess} is in the word.")
                    
                    if all(letter in guessed_letters for letter in secret_word):
                        print(f"\nCongratulations! You guessed the word: {secret_word.upper()}")
                        total_score += 10
                        print(f"Current Score: {total_score}")
                        break
                else:
                    print(f"Incorrect. {guess} is not in the word.")
                    incorrect_guesses += 1
                    
                    if incorrect_guesses == max_attempts:
                        print(HANGMAN_STAGES[incorrect_guesses])
                        print(f"\nGame Over! Out of attempts. The word was: {secret_word.upper()}")
                        print(f"Final Score: {total_score}")
                        break
        else:
            print("Invalid selection. Please enter a valid number.")
