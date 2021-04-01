import random


def main():
    trees = Drzewa(100)
    trees.sort()
    trees.zapisz('plik.txt', ',')
    trees.wypiszwagi()


class Drzewa:
    def __init__(self, n: int):
        self.__N = n
        self.trees = [Grafy(10) for i in range(self.__N)]

    def sort(self):
        n = 1
        while n is not 0:
            n = 0
            for i in range(self.__N-1):
                if self.trees[i].weight > self.trees[i + 1].weight:
                    self.trees[i], self.trees[i+1] = self.trees[i+1], self.trees[i]
                    n += 1

    def ilosc(self):
        return self.__N

    def wypiszwagi(self):
        for i in self.trees:
            print(str(i.weight))

    def wypiszmacierze(self):
        for i in self.trees:
            for j in i.tree:
                print(j, end="\n")
            print("\n")


    def zapisz(self, plik: str, separator: str):
        drzewa_string = [[[str(i) for i in j] for j in k.tree] for k in self.trees]
        wagi_string = [str(k.weight) for k in self.trees]
        with open(plik, 'w', encoding='utf-8') as file:
            counter = 1
            for macierz, waga, drzewo in zip(drzewa_string, wagi_string, self.trees):
                file.write("Drzewo nr: {}\n\n".format(str(counter)))
                for i in macierz:
                    file.write(separator.join(i) + "\n")
                file.write("\nKrawędzie: ")
                for i in drzewo.points:
                    file.write(str(i) + " ")
                file.write("\nWaga: {}\n\n\n".format(waga))
                counter += 1
        plik = str(plik).split('.')[0] + ".csv"
        with open(plik, 'w', encoding='utf-8') as file2:
            file2.write("E1,E2,E3,E4,E5,E6,E7,E8,E9,Waga\n")
            for i, j in zip(self.trees, wagi_string):
                for k in i.points:
                    file2.write(k + ",")
                file2.write(j+"\n")

class Grafy:
    def __init__(self, v: int):
        self.points = []
        self.__v = v  # v-vertices
        self.__adj = [[0 for i in range(self.__v)]
                      for j in range(self.__v)]
        self.tree = [[0 for i in range(self.__v)]
                     for j in range(self.__v)]
        self.generujmacierz()
        self.generujdrzewo()
        self.weight: int

    def generujmacierz(self):
        L = 0
        for i in range(self.__v):
            for j in range(i + 1, 10):
                L = L + 1
                self.__adj[i][j] = self.__adj[j][i] = L
        for i in range(self.__v):
            self.__adj[i][i] = 0

    def wyswietlmacierz(self):
        for i in self.__adj:
            print(i, end="\n")
        print("\n")

    def wyswietldrzewo(self):
        for i in self.tree:
            print(i, end="\n")
        print("\n")

    def generujdrzewo(self):
        r = [i for i in range(self.__v)]
        nr = 10
        nt = 0
        t = []
        weight = 0
        for i in range(self.__v - 1):
            if i == 0:
                random_r = random.choice(r)
                r.remove(random_r)
                t.append(random_r)
                random_r_2 = random.choice(r)
                r.remove(random_r_2)
                t.append(random_r_2)
                nt = nt + 1
                nr = nr - 1
                self.points.append(str(random_r) + str(random_r_2))
                self.tree[random_r][random_r_2] = self.tree[random_r_2][random_r] = self.__adj[random_r][random_r_2]
                weight = weight + self.tree[random_r_2][random_r]
            if 0 < i < self.__v-2:
                random_t = random.choice(t)
                random_r = random.choice(r)
                r.remove(random_r)
                t.append(random_r)
                nt = nt + 1
                nr = nr - 1
                self.points.append(str(random_t) + str(random_r))
                self.tree[random_t][random_r] = self.tree[random_r][random_t] = self.__adj[random_t][random_r]
                weight = weight + self.tree[random_r][random_t]
            if i == self.__v-2:
                random_t = random.choice(t)
                lr = random.choice(r)
                r.remove(lr)
                t.append(lr)
                nt = nt + 1
                nr = nr - 1
                self.points.append(str(random_t) + str(lr))
                self.tree[random_t][lr] = self.tree[lr][random_t] = self.__adj[random_t][lr]
                weight = weight + self.tree[lr][random_t]
        self.weight = weight


if __name__ == '__main__':
    main()
