import json



def add_phrases(dictionary:dict):

    # Шаблон импортированных интентов 
    base = { "path": "", "description": None, "answer": None, "customData": None, "enabled": True, "phrases": [], "patterns": None, "slots": None}

    for key in dictionary.keys():
        base["path"] = f"/{key}"
        for el in dictionary[key]:
            base["phrases"].append({ "text": f"{el}", "entities": None })
    return base





