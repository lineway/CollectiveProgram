# coding:utf-8
from math import sqrt

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0,
                     'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Mattews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0,
                     'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}
}


def sim_distance(prefs, person1, person2):
    '''
    返回一个有关person1和person2的基于距离的相似度评价（欧几里得距离）
    :param prefs: 样本数据
    :param person1: 个体1
    :param person2: 个体2
    :return: 相关系数
    '''
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if
                          item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))


def sim_pearson(prefs, person1, person2):
    '''
    返回person1和person2的皮尔逊相关系数
    :param prefs: 样本数据
    :param person1: 个体1
    :param person2: 个体2
    :return: 相关系数
    '''
    # 得到两者都曾评价过的物品列表
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 得到列表元素的个数
    n = len(si)
    # 如果两者没有共同之处，则返回 1
    if n == 0:
        return 1

    # 对所有偏好求和
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    # 求平方和
    sum1Sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[person2][it], 2) for it in si])

    # 求乘积之和
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

    # 计算皮尔逊评价值
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
    if den == 0:
        return 0
    r = num/den
    return r

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    '''
    从反映偏好的字典中返回最为匹配者，返回结果的个数和相似度函数均为可选参数
    :param prefs: 数据字典
    :param person: 比较源
    :param n: 取相似度较高的前n位
    :param similarity: 相似度度量函数
    :return:
    '''
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    # 对列表进行排序，评价值最高者排在前面（先排序，再反序，将得分高者排在前面）
    scores.sort()
    print(scores)
    scores.reverse()
    print(scores)
    return scores[0:n]
