import sys

def main():
    contributors = {}
    projects ={}
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        cont,pro = map(int,f.readline().rstrip('\n').split(' '))
        for i in range(cont):
            pcont, skill_count = f.readline().rstrip('\n').split(' ')
            skill_count = int(skill_count)
            contributors[f'{pcont}'] = {'skill_count': skill_count, 'skills': {}}
            for j in range(skill_count):
                pskill,level = f.readline().strip('\n').split(' ')
                contributors[f'{pcont}']['skills'][f'{pskill}'] =  int(level)
        print(contributors)            
        quit()
        for i in range(pro):
            preproject,*info = f.readline().rstrip('\n').split(' ')
            projects[f'{preproject}']= {'duration': 0, 'score': 0,'best_before': 0 ,'roles': 0, 'skills_needed': {}}
            info = list(map(int,info))
            projects[f'{preproject}']['duration'] = info[0]
            projects[f'{preproject}']['score'] = info[1]
            projects[f'{preproject}']['best_before'] = info[2]
            projects[f'{preproject}']['roles'] = info[3]
            for i in range(projects[f'{preproject}']['roles']):
                preskill,slevel = f.readline().rstrip('\n').split(' ')
                slevel = int(slevel)
                projects[f'{preproject}']['skills_needed'][f'{preskill}'] = slevel
    
    print(projects)
    for key in projects:
        lcontributors = []
        skills = list(projects[key]['skills_needed'].items())
        # print(skills)
        for item in contributors:
            pcontskills = list(contributors[item]['skills'].items())
            for i in skills:
                for j in pcontskills:
                    # print(pcontskills)
                    # print(j[1])
                    if abs(i[1] - j[1]) == 1:
                        # print(j)
                        lcontributors.append(item)
        print(lcontributors)
        print(f'{key} done')
if __name__ == "__main__":
    main()
