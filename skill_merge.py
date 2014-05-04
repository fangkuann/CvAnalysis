__author__ = 'fangkuan'
import jieba
skills = []
for line in open('./data/skill_lib.txt'):
    line = line.strip()
    skill = line.split('\t')[0]
    skills.append(skill)


final = []
label = [0 for i in xrange(len(skills))]
count =0
for i in xrange(len(skills)):
    if label[i] == 1:
        continue
    final.append([skills[i]])

    for j in xrange(i+1, len(skills)):
        words = jieba.cut(skills[j])
        for word in words:
            if word == skills[i]:
                final[count].append(skills[j])
                label[j] = 1
                #print skills[i] ,'\t', skills[j]
    count += 1
fout = open('./data/skill_merge.txt', 'w')
for i in xrange(len(skills)):
    fout.write('\t'.join(final[i])+'\n')
fout.flush()
fout.close()

