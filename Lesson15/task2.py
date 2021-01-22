'''
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you
to add workers to a Boss. You're not allowed to add instances of Boss class to workers
list directly via access to attribute, use getters and setters instead!

id_ - is just a random unique integer
'''
from random import randint


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, new_worker):
        if not self.has_worker_id(new_worker.id):
            self._workers.append(new_worker)

    def generate_worker_id(self):
        id = randint(1, 100)
        if self.has_worker_id(id):
            return self.generate_worker_id()
        return id

    def has_worker_id(self, id):
        return any(True for worker in self._workers if id == worker.id)

    def __str__(self):
        return f'{self.name, self.company}'

    def __repr__(self):
        return self.__str__()


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss: Boss):
        self._boss = new_boss

    def __str__(self):
        return f'{self.id} {self.name}: {self.company}, {self.boss}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    boss = Boss(1, "Ivan", "GL")
    worker1 = Worker(boss.generate_worker_id(), "Serg", "GL", boss)
    worker2 = Worker(boss.generate_worker_id(), "Dmyt", "GL", boss)
    boss.add_worker(worker1)
    boss.add_worker(worker2)
    print(
        boss
            .workers[0]
            .boss
            .workers[0]
            .boss
            .workers[0]
            .boss
    )
