from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)


def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2: return "Weak"
    elif score <= 4: return "Medium"
    else: return "Strong"


# -------------------------------
# Home Page - Now completely blank by default
# -------------------------------
@app.route('/')
def home():
    return render_template(
        "index.html",
        password="",
        strength="",
        length="",         # FIX: No default length filled in
        uppercase=False,   # FIX: Unchecked by default
        lowercase=False,   # FIX: Unchecked by default
        numbers=False,     # FIX: Unchecked by default
        symbols=False      # FIX: Unchecked by default
    )


# -------------------------------
# Generate Password
# -------------------------------
@app.route('/generate', methods=['POST'])
def generate():
    try:
        length_input = request.form.get("length")
        if not length_input:
            raise ValueError
        
        length = int(length_input)
        if length < 4 or length > 64:
            raise ValueError
            
    except (ValueError, TypeError):
        return render_template(
            "index.html",
            password="Please enter a valid password length!",
            strength="",
            length="",
            uppercase=False,
            lowercase=False,
            numbers=False,
            symbols=False
        )

    uppercase = request.form.get("uppercase") is not None
    lowercase = request.form.get("lowercase") is not None
    numbers = request.form.get("numbers") is not None
    symbols = request.form.get("symbols") is not None

    characters = ""
    password = []

    if uppercase:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if lowercase:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if numbers:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if characters == "":
        return render_template(
            "index.html",
            password="Please select at least one character type!",
            strength="",
            length=length,
            uppercase=uppercase,
            lowercase=lowercase,
            numbers=numbers,
            symbols=symbols
        )

    while len(password) < length:
        password.append(secrets.choice(characters))

    sr = secrets.SystemRandom()
    sr.shuffle(password)

    password = "".join(password)
    strength = password_strength(password)

    return render_template(
        "index.html",
        password=password,
        strength=strength,
        length=length,
        uppercase=uppercase,
        lowercase=lowercase,
        numbers=numbers,
        symbols=symbols
    )


if __name__ == "__main__":
    app.run(debug=True)