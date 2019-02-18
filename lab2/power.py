import numpy as np
import pandas as pd

def power(sample1, sample2, reps, size, alpha,):
    count =0
    for i in range(reps):

        def power(sample1, sample2, reps, size, alpha, K_iterations):
            count = 0
            for i in range(reps):
                Sam1 = np.random.choice(sample1, sample1.shape[0])
                Sam2= np.random.choice(sample2, sample2.shape[0])
                pValue = abTest(Sam1, Sam2, size)
                if (pValue < 1 - alpha):
                    count = count + 1
            return count / reps

        df = pd.read_csv('./vehicles.csv')
        sample1 = df.values.T[0]
        sample2 = df.values.T[1][0:79]
        p = power(sample1, sample2, 10000, 30, 0.6, 10)
        print(p)