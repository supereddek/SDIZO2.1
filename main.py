# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ListGraph import *
from Kruskal import *
from MatrixGraph import *
from BelmanFord import *
from Dijkstra import *
from Prim import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    h = MatrixGraph(0)
    h.make_from_file()
    print(matrix_kruskal(h))

    j = ListGraph(0)
    j.make_from_file()
    print(list_kruskal(j))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
