has_key = True
if has_key:
    outcome = ("Click: Escaping is my destiny! This key is my ticket out of here.")
    good = r"""
              .--.
              /.-. '----------.
              \'-' .--"--""-"-'
           jgs '--'"""
else:
    outcome = ("Doom: I need to find a key to unlock this door!!")
    bad = r"""
         __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________|


"""
print(outcome)
print(good)