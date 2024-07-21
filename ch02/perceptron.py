import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -theta
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -theta
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = -theta
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)
