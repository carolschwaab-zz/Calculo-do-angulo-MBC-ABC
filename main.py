import math

def calc_angle_mbc(a, b):
    degrees = round((math.atan(a / b)) * 180 / math.pi)
    return degrees