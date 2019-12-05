from datetime import datetime
import time


class Loger:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'a', encoding='utf8')
        global program_start
        program_start = datetime.now()
        self.file.write(f'program started at {program_start}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
          program_stop = datetime.now()
          self.file.write(f'\n{program_stop}ERROR {exc_type} {exc_val}')
        program_stop = datetime.now()
        self.file.write(f'\nprogram stop at {program_stop}')
        delta_time =  program_stop - program_start
        self.file.write(f'\nprogram work {delta_time.min} min, {delta_time.seconds} seconds\n')


    def timer(self):
        while True:
            answer = input("Хотите включить таймер на 3 секунды? Y- да, N - нет, E - выйти: ")
            self.file.write(f'\nAt {datetime.now()} ask question about timer\n')
            if answer == "Y":
                self.file.write(f'\nAt {datetime.now()} he input Y\n')
                print("Таймер включен")
                time.sleep(3)
                print("3 секунды прошло")
            elif answer == "N":
                self.file.write(f'\nAt {datetime.now()} he input N\n')
                print("Подожду 2 секунды и спрошу вас еще раз")
                time.sleep(2)
                print("2 секунды прошло, возращаюсь к вопросу")
            elif answer == "E":
                self.file.write(f'\nAt {datetime.now()} he input E\n')
                print("Пока")
                break
            else:
                self.file.write(f'\nAt {datetime.now()} he input something wrong\n')
                print("Ты что то не то ввел")

if __name__ == '__main__':
    with Loger('log.txt') as log:
        log.timer()
