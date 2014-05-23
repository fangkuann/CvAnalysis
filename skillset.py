# coding=utf-8
__author__ = 'fangkuan'
import collections
count = 0
skillset = []
for line in open('./data/job_skill2.txt'):
    line = line.strip()
    skill = line.split('\t')[0].replace(' ', '').lower()
    if skill.find(',') != -1:
        #print skill
        skillset+=(skill.split(','))
        count += 1
        continue

    elif skill.find('/') != -1:
        skillset+=(skill.split('/'))
        count += 1
        continue
    else:
        skillset.append(skill)


C = collections.Counter(skillset)
most_common = C.most_common(10000)
print most_common

fout = open('./data/job_lib2.txt', 'w')
for skill in most_common:
    fout.write(skill[0]+'\t'+str(skill[1])+'\n')
fout.flush()
fout.close()