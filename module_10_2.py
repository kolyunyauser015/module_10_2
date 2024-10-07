from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        number_enemies = 100
        number_days = 0
        while number_enemies > 0:
            number_days += 1
            if number_enemies > self.power:
                number_enemies -= self.power
            else:
                number_enemies = 0
            print(f"{self.name} сражается {number_days} день(дня)..., осталось {number_enemies} воинов.")
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
