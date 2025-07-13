import numpy as np


def rmse(df1, df2, variables):
    rmse = 0
    for v in variables:
        rmse += np.sqrt(np.mean((df1[v] - df2[v]) ** 2))
    rmse = rmse / len(variables)
    return rmse


def n_steps(df1, df2, variables, step=5):
    res = []
    for i in range(step):
        res.append(rmse(df1, df2, variables))
    return np.mean(res)
