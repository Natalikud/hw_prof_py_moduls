from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    dt_now = datetime.datetime.now()
    #создала переменную dt_now
    #которая через модуль datetime вызовет класс datetime и метод класса с названием def now()
    print(dt_now)

