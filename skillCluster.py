__author__ = 'fangkuan'
from sklearn import decomposition
from sklearn import feature_extraction
from sklearn import cluster
data = []
skillset= []


def readmatrix():
    fin = open('./job_keywords.txt','r')
    for line in fin:
 #       data.append({})
        line = line.strip()
        try:
            skill = line.split('\t')[0]
            jobs = line.split('\t')[1] #.split(',')
        except Exception:
            continue
        data.append(jobs)
        skillset.append(skill)
        # for job in jobs:
        #     data[-1][job] = 1
    fin.close()


readmatrix()
#data=["I am a boy","I am a girl","I am not a girl","I am not a boy"]
n_components = 20
lsa = decomposition.TruncatedSVD(n_components =n_components)
#vectorizer = feature_extraction.DictVectorizer(sparse=False)

vectorizer = feature_extraction.text.CountVectorizer(min_df = 0)

X = vectorizer.fit_transform(data)
Y = lsa.fit_transform(X)


k_means = cluster.KMeans(n_clusters = 10000)
labels = k_means.fit_predict(Y)
labelSkill = {}
for i in xrange(len(labels)):
    if labels[i] not in labelSkill:
        labelSkill[labels[i]] = [skillset[i]]
    else:
        labelSkill[labels[i]].append(skillset[i])

fout = open('./data/skill_group.txt','w')
for label in labelSkill:
    fout.write(','.join(labelSkill[label])+'\n')
fout.flush()
fout.close()