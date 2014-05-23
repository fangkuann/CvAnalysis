__author__ = 'fangkuan'
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pickle


def skill_tfidf_weight():
    job_skill = []
    job_list = []
    for line in open('./data/job_skill2.txt', 'r'):
        line = line.strip()
        if len(line.split('\t')) > 1:
#            print line
            job = line.split('\t')[0]
            skills = line.split('\t')[1]
            job_skill.append(skills)
            job_list.append(job)
    unigram_vectorizer = CountVectorizer()
    unigram_vectorizer.fit_transform(job_skill)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(unigram_vectorizer.fit_transform(job_skill))
    fout =open('./data/skill_weight.txt', 'w')
    pickle.dump(tfidf, fout)
skill_tfidf_weight()