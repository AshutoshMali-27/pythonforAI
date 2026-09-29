class team:
    def __init__(self,members):
        self.members=members;

    def __len__(self):
        return len(self.members);


team=team(["ashutosh","ashu","ashu1","ashu2"]);

print(len(team));