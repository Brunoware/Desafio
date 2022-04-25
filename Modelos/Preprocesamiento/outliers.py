# Se impora la libreria para plotear
import matplotlib.pyplot as plt


def boxplot (df,list_columns):
    for columna in list_columns:
        df.boxplot(column = columna)
        plt.title(columna)
        plt.show()