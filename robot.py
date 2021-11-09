# casual_string = "Nobody expects the Spanish inquisition! And you?!"
# casual_string_no_chars = casual_string.strip("?")
# print(casual_string.strip("!?!"))


def what_to_do(instructions):
    if instructions.startswith("Simon says") or instructions.endswith("Simon says"):
        stripped_instruction =  instructions.strip("Simon says")
        print(stripped_instruction)
        return f"I {instructions}"
    else:
        return "I won't do it"

"""  """
print(what_to_do("Simon says go excersice Simon says"))



print("""' 
' " '
' " ' " '
' " ' " ' " ' """)