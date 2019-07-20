import json

with open('cv.json', 'r') as infile:
    cv = json.load(infile)


def sort_key(entry):
    if 'when' in entry:
        return entry['when']
    return 1


for section in cv['sections']:
    section['section_entries'].sort(key=sort_key, reverse=True)

print(json.dumps(cv))
