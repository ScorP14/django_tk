class Defect:
    def __init__(self, temp: int):
        self.temp = temp

    def print(self):
        raise NotImplementedError()


class OkDefect(Defect):
    def print(self):
        print(f'Ok {self.temp}')


class InitialDefect(Defect):
    def print(self):
        print(f'Начальный {self.temp}')


class DevelopedDefect(Defect):
    def print(self):
        print(f'Развивабщий {self.temp}')


class EmergencyDefect(Defect):
    def print(self):
        print(f'Аварийный {self.temp}')


class CalkTemp:
    """Класс для расчета температур"""
    def __init__(self, t_env: int | float, t_a: int | float, t_b: int | float, t_c: int | float) -> None:
        self.t_env = t_env
        self.t_a = t_a
        self.t_b = t_b
        self.t_c = t_c

    def get_max_temp(self) -> int | float:
        """Получить максимальную температуру по фазам"""
        return max(self.t_a, self.t_b, self.t_c)

    def get_min_temp(self) -> int | float:
        """Получить минимальную температуру по фазам, но не ниже 0"""
        min_temp = min(self.t_a, self.t_b, self.t_c)
        return min_temp if min_temp > 0 else 0

    def get_overheat(self) -> int | float:
        """Температура перегрева"""
        return self.get_max_temp() - self.t_env

    def get_excess(self) -> int | float:
        """Избыточная температура между фазами"""
        return self.get_max_temp() - self.get_min_temp()

    def result(self) -> int | float:
        """Возвращает результат"""
        return self.get_overheat() if self.get_overheat() > self.get_excess() else self.get_excess()


class CalkPrint:
    def __init__(self, calk: CalkTemp):
        self.calk = calk

    def get_type_defect(self):
        temp = self.calk.result()
        strategia: Defect
        if temp in range(15):
            strategia = OkDefect(temp)
        elif temp in range(15, 25):
            strategia = InitialDefect(temp)
        elif temp in range(25, 40):
            strategia = DevelopedDefect(temp)
        elif temp >= 40:
            strategia = EmergencyDefect(temp)
        else:
            raise ValueError('Не может быть меньше 0')
        strategia.print()

    def excess_str(self) -> str:
        return f'Избыточная температура - {self.calk.get_excess()}'

    def overheating_str(self) -> str:
        return f'Температура перегрева - {self.calk.get_overheat()}'

    def temp_main_str(self) -> str:
        return self.excess_str() if self.calk.get_excess() >= self.calk.get_overheat() else self.overheating_str()


calk = CalkTemp(10, 20, 20, 30)
pr_cal = CalkPrint(calk)

print(pr_cal.get_type_defect())
