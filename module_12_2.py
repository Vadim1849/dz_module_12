import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    # def __str__(self):
    #     return self.name

    def __str__(self):
        # return f"Runner(name={self.name}, speed={self.speed})"
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        # print("self", self)
        finishers = {}
        # print("finishers", finishers)
        place = 1
        # print("place", place)
        while self.participants:
            for participant in self.participants[:]:
                # print("participant", participant)
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    # print(f"finishers[{place}] = {finishers[place]}")
                    place += 1
                    # print(f"place + 1 = {place}")
                    self.participants.remove(participant)
                    # print("finishers", finishers)
                    # Ошибка, все обновления происходят в одном цикле,
                    # при увеличении дистанции у всех участников одновременно,
                    # участники с большей скоростью могут финишировать позже,
                    # чем участники с меньшей скоростью.
        return finishers


# Код для тестирования.
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # setUp - метод, где создаются 3 объекта:
    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed=10)
        self.runner_andrei = Runner("Андрей", speed=9)
        self.runner_nik = Runner("Ник", speed=3)


    # Методы тестирования забегов,
    def test_usain_and_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_usain_and_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


    def test_andrei_and_nik(self):
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_andrei_and_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")


    def test_usain_andrei_nik(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        result = tournament.start()
        TournamentTest.all_results["test_usain_andrei_nik"] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            # print(f"{key}: {result}")
            print(f"{result}")


if __name__ == "__main__":
    unittest.main()