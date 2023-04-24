import json

def load_json(input):
    return json.loads(input)

def skip_operation(input, op, count, idx):
    return idx + count

def delete_operation(input, op, count, idx):
    input = input[:idx] + input[idx+count:]
    return input

def insert_operation(input, op, chars, idx):
    input = input[:idx] + chars + input[idx:]
    idx = idx + len(chars)
    return idx, input

def isValid(given, expected, ot):
    idx = 0
    ot = load_json(ot)
    while len(ot) > 0:
        current_ot = ot.pop(0)
        if current_ot['op'] == 'skip':
            idx = skip_operation(given,'skip',current_ot['count'], idx)
            if idx > len(given): return False
        elif current_ot['op'] == 'delete':
            given = delete_operation(given,'delete',current_ot['count'], idx)
        elif current_ot['op'] == 'insert':
            idx, given = insert_operation(given,'insert',current_ot['chars'], idx)
    return True if given == expected else False
