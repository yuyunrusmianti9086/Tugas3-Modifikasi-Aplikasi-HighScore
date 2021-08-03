class GameEntry:
    sum_player = 0

    def __init__(self, name, score, timeq):
        self.name = name
        self.score = score
        self.time = timeq
        
        GameEntry.sum_player += 1
    
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score

    def set_time(self, timeq):
        self.time = timeq

    def get_time(self):
        return self.time

    def get_sum():
        return GameEntry.sum_player

class ScoreBoard:

    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0 #number of actual entries
    
    def get_capacity(self):
        return self.capacity

    def sum_entri(self):
        return self.n

    def add_item(self, entry):
        score = entry.get_score()

        condition = len(self.board) > self.n or score > self.board[self.capacity - 1].get_score()
        # print(condition)

        if condition:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].get_score() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"Entry {score} added")

    def list_entri(self):
        for i in range (0, self.n):
            print(i+1,".", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))

#capacity
board = ScoreBoard(10)

#MENU
active = True
while active:
    print("")
    start = input("Opsi: \n 1 = Add Entry \n 2 = view List ScoreBoard \n 3 = Exit\n")
    print("")
    if start == '2':
        board.list_entri()
    elif start == '1':
        name = input("Add Name Player : ")
        score = int(input("Add Score : "))
        time= int(input("Add Time : "))

        in_score = GameEntry(name, score, time)
        set_board = board.add_item (in_score)

        print(f" New Entry Added : {in_score.get_name()} {in_score.get_score()} {in_score.get_time()}")
    else:
        break