class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.trash_items = []

    def add_trash(self,trash_item):
        self.trash_items.append(trash_item)

    def increase_score(self):
        self.score +=1
    