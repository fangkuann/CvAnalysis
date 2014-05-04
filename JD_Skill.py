__author__ = 'fangkuan'
import jieba

skills = set([])
job_skill = {}
def readSkill():
    for line in open('./data/skill_lib.txt'):
        line = line.strip()
        skill = line.split('\t')[0]
        skills.add(skill)


def readJD():
    for line in open('./data/jd.txt'):
        line = line.strip()
        job = line.split('#')[0].split(' ')[0]
        JD = line.split('#')[5]
        if job not in job_skill:
            job_skill[job]=set([])
        keywords = jieba.cut(JD, cut_all=False)
        for word in keywords:
            word = word.lower()
            if word in skills:

                job_skill[job].add(word.encode('utf8'))
 #               print word

readSkill()
readJD()
fout = open('./data/jd_skill.txt','w')
for job in job_skill:
   # print job
    fout.write(job+'\t'+','.join(job_skill[job])+'\n')
fout.flush()
fout.close()