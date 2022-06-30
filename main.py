# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ListGraph import *
from Kruskal import *
from MatrixGraph import *
from BelmanFord import *
from Dijkstra import *
from Prim import *
from TimeMeasure import *


def print_menu():
    print("Jaki problem chcesz zbadac?\n"
          "1 - MST\n"
          "2 - Najkrotsza droga\n")

    match int(input()):
        case 1:
            mst_list_menu()
        case 2:
            minimal_road_list_menu()
        case _:
            print("Niewlasciwy wybor.")
            print_menu()


def mst_list_menu():
    ls_graph = ListGraph()
    mx_graph = MatrixGraph()
    while True:
        print("Co chcesz zrobic?\n"
              "1 - wczytaj strukture z pliku\n"
              "2 -generuj losowo\n"
              "3 - wyswietl graf\n"
              "4 - Algorytm Prima\n"
              "5 - Algorytm Kruskala")
        match int(input()):
            case 1:
                ls_graph.clear()
                mx_graph.clear()
                ls_graph.make_from_file_undirected()
                mx_graph.make_from_file_undirected()
            case 2:
                ls_graph.clear()
                mx_graph.clear()
                vertices = int(input("Podaj liczbe wierzcholkow:"))
                density = float(input("Podaj gestosc (w formie ulamka dziesietnego):"))
                ls_graph.generate_random_undirected(vertices, density)
                mx_graph.generate_random_undirected(vertices, density)
            case 3:
                ls_graph.print()
                mx_graph.print()
            case 4:
                print("Algorytm Prima macierzowo:")
                print(matrix_prim(mx_graph))
                print("Algorytm Prima listowo:")
                print(list_prim(ls_graph))
            case 5:
                print("Algorytm Kruskala macierzowo:")
                print(matrix_kruskal(mx_graph))
                print("Algorytm Kruskala listowo:")
                print(list_kruskal(ls_graph))
            case 6:
                return
            case _:
                print("Niewlasiwa opcja!")


def minimal_road_list_menu():
    ls_graph = ListGraph()
    mx_graph = MatrixGraph()
    while True:
        print("Co chcesz zrobic?\n"
              "1 - wczytaj strukture z pliku\n"
              "2 -generuj losowo\n"
              "3 - wyswietl graf\n"
              "4 - Algorytm Dijkstry\n"
              "5 - Algorytm Bellmana-Forda")
        match int(input()):
            case 1:
                ls_graph.clear()
                mx_graph.clear()
                ls_graph.make_from_file_directed()
                mx_graph.make_from_file_directed()
            case 2:
                ls_graph.clear()
                mx_graph.clear()
                vertices = int(input("Podaj liczbe wierzcholkow:"))
                density = float(input("Podaj gestosc (w formie ulamka dziesietnego):"))
                ls_graph.generate_random_directed(vertices, density)
                mx_graph.generate_random_directed(vertices, density)
            case 3:
                ls_graph.print()
                mx_graph.print()
            case 4:
                start = int(input("Podaj wierzcholek startowy: "))
                dest = int(input("Podaj wierzcholek koncowy: "))
                print("Algorytm Dijkstry listowo:")
                list_dijkstra(ls_graph, start, dest)
                print("Algorytm Dijkstry macierzowo:")
                matrix_dijkstra(mx_graph, start, dest)
            case 5:
                start = int(input("Podaj wierzcholek startowy: "))
                dest = int(input("Podaj wierzcholek koncowy: "))
                print("Algorytm Bellmana-Forda listowo")
                list_bellman_ford(ls_graph, start, dest)
                print("Algorytm Bellmana-Forda macierzowo:")
                matrix_bellman_ford(mx_graph, start, dest)
            case 6:
                return
            case _:
                print("Niewlasiwa opcja!")


if __name__ == '__main__':
    print_menu()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
