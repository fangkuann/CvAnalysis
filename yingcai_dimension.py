# coding=utf-8
__author__ = 'fangkuan'
import collections
import jieba
import pymongo
from pymongo import MongoClient

dest = "192.168.4.250"
dbname = "yingcai"
client = MongoClient(dest, 27017)
db = client[dbname]
yingcai = db['yingcai_userinfo']
fin = yingcai.find()
user_dimension = db['user_dimension']
count = 0
college_loc = {}  #大学 城市表
skill_weight = {}  # 职业 技能 权值表
job_exp = {}  # 职业 最高薪金表
academic_level = {}  # 学历  等级表


def read_academic_level():
    for line in open('./data/academic_level.txt'):
        line = line.strip()
        academic, level = line.split('\t')
        academic_level[academic_level] = level


def read_job_exp():
    for line in open('./data/skill_weight.txt'):
        line = line.strip()
        job, exp = line.split('\t')
        job_exp[job] = exp


def read_skill_weight():
    for line in open('./data/skill_weight.txt'):
        line = line.strip()
        job, skill, weight = line.split('\t')
        if job in skill_weight:
            skill_weight[job][skill] = weight
        else:
            skill_weight[job] = {skill: weight}


def college_location():
    for line in open('./data/college_location.txt'):
        line = line.strip()
        college, location = line.split('\t')
        college_loc[college] = location


def major_ability(experience, exp_y_salary, pro_title, t_pre_skill, academic_name):
    skill_ability = 0.
    job_exp_ability = 0.
    time_ability = 0.
    academic_ability = 0.
    if pro_title in skill_weight:
        for skill in t_pre_skill:
            if skill in skill_weight[pro_title]:
                skill_ability += skill_weight[pro_title][skill]

    if pro_title in job_exp:
        if exp_y_salary:
            job_exp_ability += exp_y_salary / job_exp[pro_title]

    if experience:
        timelines = []
        for exp in experience:
            s_time = exp['start_time'].split('.')[0]
            e_time = exp['end_time'].split('.')[0]
            timelines.append(s_time)
            timelines.append(e_time)
        time_ability += (max(timelines) - min(timelines)) / 20.

    if academic_name:
        if academic_name in academic_level:
            academic_ability += academic_level[academic_name]

    return (skill_ability + job_exp_ability + time_ability) / 4 + academic_ability


def cal_location(exp_location, living, education):
    if exp_location:
        return exp_location[0]
    elif living:
        return living[0]
    elif education:
        for edu in education:
            college = edu['college']
            if college in college_loc:
                return college_loc[college]
        return 'null'
    else:
        return 'null'


def cal_job(pro_title, work_experience):
    if pro_title:
        return pro_title[0]
    elif work_experience:
        for work in work_experience:
            return work['job_name']
        return 'null'
    else:
        return 'null'


def cal_dimensions():
    for cv in fin:
        post = {}
        uid = cv['_id']
        pro_title = cv['pro_title']
        exp_location = cv['exp_location']
        living = cv['living']
        education = cv['education']
        work_experience = cv['experience']
        exp_y_salary = cv['exp_y_salary']
        t_pre_skill = cv['t_pre_skill']
        academic_name = cv['academic_name']
        location = cal_location(exp_location, living, education)
        job = cal_job(pro_title, work_experience)
        ability = major_ability(work_experience, exp_y_salary, pro_title, t_pre_skill, academic_name)

        post['location'] = location
        post['job'] = job
        post['ability'] = ability
        post['uid'] = uid

        user_dimension.insert(post)


college_location()
cal_dimensions()