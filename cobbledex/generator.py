import json, random

class CobbleGenerator:
    def __init__(self, json_path):
        self.json_path = json_path
        with open(json_path, "r", encoding="utf-8") as f:
            self.db = json.load(f)

    def list_all(self):
        return self.db

    def generate(self, name=None):
        base = random.choice(self.db)
        new = base.copy()
        new['id'] = max(p['id'] for p in self.db) + 1
        new['name'] = name or base['name'] + "-" + str(random.randint(1,999))
        # leve variação nos stats
        new['stats'] = {k: max(1, int(v * random.uniform(0.8,1.2))) for k,v in base['stats'].items()}
        return new
