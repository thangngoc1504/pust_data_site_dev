def detect_parse_false_choice(input_choice):
    # this parse content between A. and B. to a choice and so on to D.
    choices_with_key = input_choice[5]
    # list_choices = []
    # for choice in choices_with_key:
    #     # key = choice[:1]
    #     value = choice[3:]
    #     list_choices.append((value))

    # return list_choices
    return choices_with_key
detect_parse_false_choice('lop-2')




def correct_format(input_choice):
    correct_answer_format = input_choice[0]
    switcher={
        'A':'0',
        'a':'0',
        'B':'1',
        'b':'1',
        'C':'2',
        'c':'2',
        'D':'3',
        'd':'3'  
    }
    return switcher.get(correct_answer_format, "None")

correct_format()


def detect_parse_false_choice(input_choice):
    # this parse content between A. and B. to a choice and so on to D.
    choices_with_key = input_choice.split("\n")
    dict_choices = {}
    for choice in choices_with_key:
        key = correct_format(choice[:1])
        value = choice[3:]
        dict_choices[key] = value
    return dict_choices





