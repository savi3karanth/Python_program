
pin = "1234"
trails = 1

while trails <= 3:
    input_pin = input(f"Trail-{trails} | PIN>> ")
    trails += 1
    if input_pin == pin:
        print("Correct pin")
        break
    else:
        print("Incorrect pin please try again")
