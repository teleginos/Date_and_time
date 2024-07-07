from datetime import datetime


class SuperDate(datetime):
    def get_season(self):

        month = self.month
        month_dict = {(12, 1, 2): 'Winter', (3, 4, 5): 'Spring', (6, 7, 8): 'Summer', (9, 10, 11): 'Autumn'}
        for key, value in month_dict.items():
            if month in key:
                return value

    def get_time_of_day(self):
        hour = self.hour
        time_of_day_dict = {(6, 12): 'Morning', (12, 18): 'Day', (18, 24): 'Evening', (0, 6): 'Night'}
        for key, value in time_of_day_dict.items():
            if key[0] <= hour < key[1]:
                return value


if __name__ == '__main__':
    try:
        a = SuperDate(2024, 2, 22, 12)
        print(a.get_season())
        print(a.get_time_of_day())
    except ValueError as err:
        print(f"Некорректный ввод данных: {err}")
