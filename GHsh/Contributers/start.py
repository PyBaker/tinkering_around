
from datetime import datetime
from re import S


class Contributors:
    name:str=""
    skill = {}

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

class Project:
    name:str=""
    skills = []
    duration = None
    best_before = None
    score = None

    contirbutors = {}
    def __init__(self, name, skills, duration, best_before, score):
        self.name = name
        self.skills = skills
        self.duration = duration
        self.best_before = best_before
        self.score = score
    
    def AssignContributor(self, contributor:Contributors):
        self.contirbutors[contributor.name] = contributor.skill

class Roles:
    name:str=""
    level:int=0


def loaddata(contributors, projects, filecontents=[]):
    parsedata = {}
    cont = []
    projobj = []
    iterator = 0
    total = len(filecontents)
    track_cont = 0
    track_proj = 0
    while(iterator < total):
        if track_cont < contributors and track_proj == 0:
            line = filecontents[iterator]
            name, skillcount = line.split(' ')
            skillcount = int(skillcount)
            skills = {}
            for i in range(skillcount):
                skillname, level = filecontents[iterator + i].split()
                skills[skillname] = int(level)
            iterator = iterator + skillcount
            track_cont = track_cont + 1
            con = Contributors(name, skills)
            cont.append(con)
        elif track_proj < projects and track_cont == contributors:
            line = filecontents[iterator]
            name, duration, score, best_before, skill_needed = line.split()
            skills = []
            skill_needed = int(skill_needed)
            for i in range(skill_needed):
                skills.append(filecontents[iterator + i])
            iterator = iterator + skill_needed
            pro = Project(name, skills, duration, best_before, score)
            projobj.append(pro)
        iterator = iterator+1
    print(cont)
    print([j.todict() for j in projobj])

with open('data.txt', 'r') as f:
    filecontents = f.readlines()
    fileparsed = [i.split('\n')[0] for i in filecontents]
    cont, proj = map(int,fileparsed[0].split())
    fp = fileparsed[1:]
    loaddata(cont, proj, fp)


