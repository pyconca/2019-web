"""
List of talk IDs
"""
import json
import os

schedule_truth = "../../data/speakers-details.json"

TALK_IDS = [
    11,
    15,
    23,
    25,
    33,
    44,
    82,
    86,
    87,
    88,
    89,
    95,
    96,
    97,
    99,
    100,
    109,
    112,
    113,
    114,
    119,
    122,
    129,
    143,
    144,
    146,
    147,
    148,
    153,
    154,
    155,
    157,
    160,
    169,
    172,
    179,
    180,
    195,
    199,
    201,
    203,
    209,
    211,
    215,
    221,
    223,
    225,
    378
]


if os.path.isfile(schedule_truth):
    schedule_data = json.loads((open(schedule_truth).read()))
    TALK_IDS = sorted([x["ID"] for x in schedule_data])

if __name__ == "__main__":
    print(TALK_IDS)
