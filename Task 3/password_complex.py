import argparse
from termcolor import colored

def check_password_strength(password):
    length_okay = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(not char.isalnum() for char in password)

    # Calculate strength score based on criteria
    strength_score = sum([length_okay, uppercase, lowercase, digit, special_char])

    # Visual representation using text-based characters
    visual_strength = ''
    if length_okay:
        visual_strength += '|'
    else:
        visual_strength += ' '
    if uppercase:
        visual_strength += '|'
    else:
        visual_strength += ' '
    if lowercase:
        visual_strength += '|'
    else:
        visual_strength += ' '
    if digit:
        visual_strength += '|'
    else:
        visual_strength += ' '
    if special_char:
        visual_strength += '|'
    else:
        visual_strength += ' '

    # Provide feedback based on strength score
    if strength_score == 5:
        strength_result = colored("Strong password", 'green')
    elif strength_score >= 3:
        strength_result = colored("Medium password", 'yellow')
    else:
        strength_result = colored("Weak password", 'red')

    return strength_result, visual_strength

def main():
    parser = argparse.ArgumentParser(description="Check the strength of a password")
    parser.add_argument("-p", "--password", type=str, required=True, help="The password to check")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")
    args = parser.parse_args()
    
    strength_result, visual_strength = check_password_strength(args.password)
    print("Password Complexity Visualization:")
    print(visual_strength)
    print("Password Strength Assessment:")
    print(strength_result)

if __name__ == "__main__":
    main()