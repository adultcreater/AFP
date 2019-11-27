import json

DEFAULT_MESSAGE = {}

def save(contents, module):
    with open(f'config/{module}.json', 'w', encoding= 'utf-8') as f:
        return json.dump(contents, f, ensure_ascii=False, indent=4)

def load(module):
    try:
        with open(f'config/{module}.json', encoding='utf-8') as f:
            return json.load(f)

    except OSError:
        
        save(DEFAULT_MESSAGE, module)