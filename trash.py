class TrashItem:
    def __init__(self,name,correct_choice,choices):
        self.name = name
        self.correct_choice = correct_choice
        self.choices = choices
    
    
    def check_disposal(self,player_choice):
        if player_choice == self.correct_choice:
            return "정답입니다!"
        else:
            corret_answer = self.choices[self.correct_choice-1]
            return f"틀렸습니다.올바른 분리수거 방법은\n'{corret_answer}'입니다."
        
    def __str__(self):
        return f"TrashItem(name='{self.name}', choices={self.choices})"