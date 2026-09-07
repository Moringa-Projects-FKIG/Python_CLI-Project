class Suspect:
    def __init__(self, name, occupation, motive, clothing, alibi, secret):
        self.name = name
        self.occupation = occupation
        self.motive = motive
        self.clothing = clothing
        self.alibi = alibi
        self.secret = secret

    def introduction(self):
        return f"{self.name}: I was at the gala."


class Chef(Suspect):
    def introduction(self):
        return f"{self.name}: I was working in the kitchen."


class Businessman(Suspect):
    def introduction(self):
        return f"{self.name}: I was talking to guests."


class Journalist(Suspect):
    def introduction(self):
        return f"{self.name}: I was interviewing guests."


class Manager(Suspect):
    def introduction(self):
        return f"{self.name}: I was checking hotel rooms."


SUSPECTS = [
    Chef("Lance", "Chef", "Hassan planned to fire him.",
         "White chef jacket and silver watch.",
         "He says he was in the kitchen.", "He was about to lose his job."),

    Businessman("Chris", "Businessman", "Hassan knew about his debts.",
                "Navy suit and silver tie.", "He says he was with his girlfriend.",
                "He owed the hotel a large amount of money."),

    Journalist("Melody", "Journalist", "Hassan knew a dangerous family secret.",
                "Black blazer with silver buttons.", "She says she was interviewing guests.",
                "She was protecting her brother."),

    Manager("Michael", "Hotel Manager", "Hassan discovered missing hotel money.",
            "Dark grey suit and hotel badge.", "He says he was checking rooms.",
            "He had been secretly taking hotel money.")
]
