import statistics
import numpy as np
import seaborn as sn
from matplotlib import pyplot as plt

def main():
    aux = []

    with open("example2.txt", 'r') as file:
        while(1):

            a = file.readline()
            if(a == ''):
                break
            else:

                aux.append(int(a))

    print("Total de amostras: {}".format(len(aux)))
    print("Mínimo: {}".format(min(aux)))
    print("Média: {}".format(round(statistics.mean(aux))))
    print("Maximo: {}".format(max(aux)))
    print("Desvio-padrão: {}".format(np.std(aux)))



    res = sn.kdeplot(aux, color='green', shade=True)

    plt.show()




if __name__ == "__main__":
    main()





