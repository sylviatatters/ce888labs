import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
matplotlib.use('Agg')


def mad(array):
    array = np.ma.array(array).compressed()
    Median = np.median(array)
    return np.median(np.abs(array-Median))


if __name__ == "__main__":
    df = pd.read_csv('M:\\datascience\ce888labs\lab2\\vehicles.csv')
    print((df.columns))
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("scaterplot.png", bbox_inches='tight')
    sns_plot.savefig("scaterplot.pdf", bbox_inches='tight')

    data = df.values.T[1,0:79]

    print((("Mean: %f") % (np.mean(data))))
    print((("Median: %f") % (np.median(data))))
    print((("Var: %f") % (np.var(data))))
    print((("std: %f") % (np.std(data))))
    print((("MAD: %f") % (mad(data))))

    plt.clf()
    sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('Millons of pounds in sales')
    axes.set_ylabel('Sales count')

    sns_plot2.savefig("histogram.png", bbox_inches='tight')
    sns_plot2.savefig("histogram.pdf", bbox_inches='tight')
