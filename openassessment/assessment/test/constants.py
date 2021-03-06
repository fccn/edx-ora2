# -*- coding: utf-8 -*-
"""
Constants used as test data.
"""

STUDENT_ITEM = {
    'student_id': u'๐ฝ๐ฎ๐ผ๐ฝ ๐ผ๐ฝ๐พ๐ญ๐ฎ๐ท๐ฝ',
    'item_id': u'๐๐๐๐ ๐๐๐๐',
    'course_id': u'ีัเธฃี ฯเนเธขะณเธฃั',
    'item_type': u'openassessment'
}

ANSWER = {'text': u'แบรซแนกแบ รคแนแนกแบรซแน'}

RUBRIC_OPTIONS = [
    {
        "order_num": 0,
        "name": u"๐๐๐๐",
        "explanation": u"๐ป๐๐๐ ๐๐๐!",
        "points": 0,
    },
    {
        "order_num": 1,
        "name": u"๐ฐ๐ธ๐ธ๐ญ",
        "explanation": u"๏ปญัปัปษ ๏ปัปเน!",
        "points": 1,
    },
    {
        "order_num": 2,
        "name": u"ัฯยขัโโัฮทั",
        "explanation": u"ไน๏พcไน๏พ๏พไนๅ๏ฝฒ ๏พoไน!",
        "points": 2,
    },
]

RUBRIC = {
    'prompts': [{"description": u"ะะพัะ-โััะบ; ะพั, ะะั ะฉะะฐlั"}],
    'criteria': [
        {
            "order_num": 0,
            "name": u"vรธศผศบฦแตพลศบษษ",
            "prompt": u"ฤฆรธw vศบษษจษฤ ษจs ลงฤงษ vรธศผศบฦแตพลศบษษ?",
            "options": RUBRIC_OPTIONS
        },
        {
            "order_num": 1,
            "name": u"๏ปญษผเธเนเนเธษผ",
            "prompt": u"๐ณ๐๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐ ๐๐๐๐๐๐๐?",
            "options": RUBRIC_OPTIONS
        }
    ]
}

RUBRIC_POSSIBLE_POINTS = sum(
    max(
        option["points"] for option in criterion["options"]
    ) for criterion in RUBRIC["criteria"]
)

# Used to generate OPTIONS_SELECTED_DICT. Indices refer to RUBRIC_OPTIONS.
OPTIONS_SELECTED_CHOICES = {
    "none": [0, 0],
    "few": [0, 1],
    "most": [1, 2],
    "all": [2, 2],
}

OPTIONS_SELECTED_DICT = {
    # This dict is constructed from OPTIONS_SELECTED_CHOICES.
    # 'key' is expected to be a string, such as 'none', 'all', etc.
    # 'value' is a list, indicating the indices of the RUBRIC_OPTIONS selections that pertain to that key
    key: {
        "options": {
            RUBRIC["criteria"][i]["name"]: RUBRIC_OPTIONS[j]["name"] for i, j in enumerate(value)
        },
        "expected_points": sum(
            RUBRIC_OPTIONS[i]["points"] for i in value
        )
    } for key, value in OPTIONS_SELECTED_CHOICES.iteritems()
}

EXAMPLES = [
    {
        'answer': (
            u"๐ฟ๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐"
            u" ๐๐๐๐ ๐ ๐๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐ ๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐ ๐๐๐๐, ๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐"
            u" ๐๐ ๐๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐, ๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐ ๐๐ ๐๐๐๐๐๐'๐ ๐๐๐๐๐๐๐ ๐๐๐ ๐๐๐ ๐๐๐."
        ),
        'options_selected': {
            u"vรธศผศบฦแตพลศบษษ": u"๐ฐ๐ธ๐ธ๐ญ",
            u"๏ปญษผเธเนเนเธษผ": u"๐๐๐๐",
        }
    },
    {
        'answer': u"Tลแน-hรฉรกvำณ แบรกล thรฉ ลhรญแน รกล รก dรญลลรฉลฤบรฉลล ลtรบdรฉลt แบรญth รกฤบฤบ รลรญลtลtฤบรฉ รญล hรญล hรฉรกd.",
        'options_selected': {
            u"vรธศผศบฦแตพลศบษษ": u"๐๐๐๐",
            u"๏ปญษผเธเนเนเธษผ": u"ัฯยขัโโัฮทั",
        }
    },
]
