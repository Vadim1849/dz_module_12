import unittest
from runner import Runner


# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
class RunnerTest(unittest.TestCase):
    # test_walk - метод, в котором
    def test_walk(self):
        # создаётся объект класса Runner с произвольным именем.
        runner = Runner("ArbitraryRunnerName")
        # Далее вызовите метод walk у этого объекта 10 раз.
        for _ in range(10):
            runner.walk()
        # После чего методом assertEqual сравните distance этого объекта со значением 50.
        self.assertEqual(runner.distance, 50)

    # test_run - метод, в котором
    def test_run(self):
        # создаётся объект класса Runner с произвольным именем.
        runner = Runner("ArbitraryRunnerName")
        # Далее вызовите метод run у этого объекта 10 раз.
        for _ in range(10):
            runner.run()
        # После чего методом assertEqual сравните distance этого объекта со значением 100.
        self.assertEqual(runner.distance, 100)

    # test_challenge - метод в котором
    def test_challenge(self):
        # создаются 2 объекта класса Runner с произвольными именами.
        runner1 = Runner("ArbitraryRunnerName1")
        runner2 = Runner("ArbitraryRunnerName2")

        # Далее 10 раз у объектов вызываются методы run и walk соответственно.
        for _ in range(10):
            runner1.run()
            runner2.walk()
        # Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
        # чтобы убедится в неравенстве результатов.
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.assertEqual(runner1.distance, 100)
        self.assertEqual(runner2.distance, 50)


if __name__ == '__main__':
    # Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
    unittest.main()
    # test_walk()
    # test_run()
    # test_challenge()