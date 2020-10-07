import application.salary as salary, application.db.people as people
from datetime import datetime
if __name__ == '__main__':
    print('Сегодня', datetime.now(tz=None))
    salary.calculate_salary()
    people.get_employees()

