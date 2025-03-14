# Importing the module
import random

# generate secret code
def create_secret_code():
    code = str(random.randint(1000, 9999))

    return code

# main function
def main():

    while True:

        secret_code = create_secret_code()
        print(secret_code)

        attemps = int(input("Enter how many do you want to try: "))

        cows = 0
        bulls = 0

        if attemps >= 0:

            for i in range(4):

                guess = input("Enter your guess (4 digits): ")

                if secret_code[i] == guess[i]:
                    secret_code.replace(secret_code[i], "")
                    bulls += 1
                    print(f"{bulls} Bulls, {cows} Cows.")
                    attemps -= 1

                elif guess[i] in secret_code:
                    cows += 1
                    print(f"{bulls} Bulls, {cows} Cows.")
                    attemps -= 1

                elif secret_code == "":
                    print(f"You guess the correct answer in {attemps} try!")
                    break

                if secret_code == "":
                    print(f"Congratulations! You  guessed the secret code {secret_code}.")
                    
                print(f"Attemps left: {attemps}")

            else:
                print(f"Game Over! The secret code was {secret_code}.")


if __name__ == "__main__":
    main()
            