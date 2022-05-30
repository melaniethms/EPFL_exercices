
for i in range(21):
    current_step = (i + 1)
    step_word = ""
    if current_step <= 9:
        step_word = " is a figure"
    else:
        step_word = " is a number"
    print("It's " + str(current_step) + str(step_word))
  