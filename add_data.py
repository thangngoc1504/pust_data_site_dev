import pandas as pd
import xlrd
import requests
import sys

ECLAZZ_API_URL = 'https://api.eclass.ftech.ai/api/crawled_questions'
ECLAZZ_HEADERS = {
  'Secret-Key': 'jf^oqzt269=(-#c@hv3$js6)#3vni5@75hed%k-9xr546jy%9p',
  'Content-Type': 'application/json',
}

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

def detect_parse_false_choice(input_choice):
    # this parse content between A. and B. to a choice and so on to D.
    choices_with_key = input_choice.split("\n")
    dict_choices = {}
    for choice in choices_with_key:
        key = correct_format(choice[:1])
        value = choice[3:]
        dict_choices[key] = value
    return dict_choices


input = 'Lop 2/data_Lop-2_mon-tieng-viet.xlsx'
newData = pd.read_excel(input,engine='openpyxl')
data = newData.to_dict('record')
for i in range(0,188,1):
    data = newData.to_dict('record')[i]
    text_content = data['text_content']
    text_answer = data['text_answer']
    correct_answer  = data['correct_answer']
    solution = data['solution']
    subject = data['subject']
    grade_level = data['grade_level']
    group = grade_level.split('-')[-1]
    chapter = data['chapter']
    lesson = data['lesson']
    name = data['name']
    source_crawler = data['source_crawler']
    format_anwser =  detect_parse_false_choice(text_answer)
    format_correct = correct_format(correct_answer)
    payload = {
        "source": 3,
        "id_source": None,
        "group": group,
        "content": {
            "format": "latex",
            "content": text_content,
        },
        "options": format_anwser,
        "correct_answers": [format_correct],
        "solution": solution,
        "source_url": source_crawler,
        "subject": 138,
        "extra_info": {
            "hint": {
                "lesson": lesson,
                "chapter": chapter
            }
        }
        }
        # payload = json.dumps(payload, ensure_ascii=False)
    response = requests.request("POST", ECLAZZ_API_URL, headers=ECLAZZ_HEADERS, json=payload)
    if response.status_code == 201:
        print(response.status_code, response.text)
    else:
        print(response.status_code, response.text)

