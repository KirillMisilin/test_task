from collections import deque

# FIFO через список
class Fifo1:
    def __init__(self):  # инициализация списка
        self.fifo_list = list()

    def add_member(self, member):  # добавление элемента в конец списка
        self.fifo_list.append(member)

    def get_member(self):  # получение и удаление из списка первого элемента
        if self.fifo_list:  # проверка на пустоту списка
            member = self.fifo_list[0]
            self.fifo_list.pop(0)
            return member
        else:
            print("Empty list")


# FIFO через двустороннюю очередь
class Fifo2:
    def __init__(self):  # инициализация очереди
        self.fifo_list = deque()

    def add_member(self, member):  # добавление элемента в конец очереди
        self.fifo_list.append(member)

    def get_member(self):  # получение и удаление из очереди первого элемента
        if self.fifo_list:
            member = self.fifo_list[0]
            self.fifo_list.popleft()
            return member
        else:
            print("Empty list")
