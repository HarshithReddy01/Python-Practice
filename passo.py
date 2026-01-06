import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter a password: ")
    
    missing = []
    
    if len(password) < 8:
        missing.append("at least 8 characters")
    if not re.search(r'[A-Z]', password):
        missing.append("an uppercase letter")
    if not re.search(r'[a-z]', password):
        missing.append("a lowercase letter")
    if not re.search(r'[0-9]', password):
        missing.append("a number")
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        missing.append("a special character")
    
    if missing:
        print(f"Password is weak. Missing: {', '.join(missing)}")
    else:
        print("Password is strong!")