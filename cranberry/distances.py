from math import sqrt
from operator import sub

def euclidean_distance(point_x, point_y):
    return sqrt(pow((point_x[0] - point_y[0]), 2) + 
                pow((point_x[1] - point_y[1]), 2))

def hamming_distance(point_x, point_y):
    return sum(set(point_x) ^ set(point_y))

def jaccard_distance(point_x, point_y):
    intersect = len(set(point_x) & set(point_y))
    union = len(set(point_x) | set(point_y))
    return intersect / union

