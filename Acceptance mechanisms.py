import math
import random
def mc_acceptance(e_temp, e_cur):
    delta = e_temp - e_cur 
    if e_temp < 1:
        delta = delta * 10000
    r = random.uniform(0,1) #creating random values between 0 and 1
    return r < pow(e,-delta)

def sa_acceptance(e_temp, e_cur):
    imprs = e_cur - e_temp
    if imprs > 0:
        n_imprs = n_imprs + 1
        mu_impr = mu_impr + (imprs - mu_impr)/n_imprs
    arg1 = imprs /(t_s * mu_impr)
    arg2 = exet / (exect - elapsed_t)
    delta = arg1 * arg2
    r = random.uniform(0,1)
    return r < delta

def ta_acceptance(e_temp, e_cur, e_best, t=100):
    if e_temp < e_cur:
        return True
    if e_temp < 1:
        t_norm = t * 0.0001
        return e_temp < e_best + t_norm
    else:
        return e_temp < e_best + t

def ie_acceptance(e_temp, e_cur):
    x = e_temp <= e_cur
    return x

def naive_acceptance(e_temp, e_cur, p = 0.5):
    if e_temp < e_cur:
        return True
    else:
        val = random.uniform(0,1)
        return val < p
