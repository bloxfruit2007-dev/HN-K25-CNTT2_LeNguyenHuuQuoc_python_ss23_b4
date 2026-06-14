import string
import random

def generate_assignment_code():
    character = string.ascii_uppercase + string.digits
    code = "".join(random.choices(character, k = 4))

    return f"PY-{code}"
