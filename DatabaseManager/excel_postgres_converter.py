import numpy as np
import psycopg2
import xlrd


class ExcelPostgresConverter:

    def __init__(self,
                 query="""INSERT INTO weather_characteristics (locality, hour_number, wind_speed, wind_temperature,
                                                    pressure, direct_solar_rad, diffuse_solar_rad, total_solar_rad) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                 book_path="D:/Work/RenewableEnergy/solarRad.xlsx"):
        self.__query = query
        self.__book_path = book_path

    def convert(self):
        book = xlrd.open_workbook(self.__book_path)
        print(book.sheet_names())
        bookName = input("Введите название населенного пункта: ")
        sheet = book.sheet_by_name(bookName)
        database = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost",
                                    port="5432")
        cursor = database.cursor()

        for r in range(1, sheet.nrows):
            locality = bookName
            hour_number = sheet.cell(r, 0).value
            wind_speed = sheet.cell(r, 1).value
            wind_temperature = sheet.cell(r, 2).value
            pressure = sheet.cell(r, 3).value
            direct_solar_rad = sheet.cell(r, 4).value
            diffuse_solar_rad = sheet.cell(r, 5).value
            total_solar_rad = sheet.cell(r, 6).value

            values = (locality, hour_number, wind_speed, wind_temperature,
                      pressure, direct_solar_rad, diffuse_solar_rad, total_solar_rad)
            cursor.execute(self.__query, values)

        cursor.close()
        database.commit()
        database.close()

        print("Data from Excel imported into postgreSQL successfully")

    def get_dataset_from_excel(self):
        book = xlrd.open_workbook(self.__book_path)
        print(book.sheet_names())
        bookName = input("Введите название населенного пункта: ")
        sheet = book.sheet_by_name(bookName)

        dataset = np.zeros(shape=(sheet.nrows, 6))

        for r in range(1, sheet.nrows):
            # hour_number = sheet.cell(r, 0).value
            wind_speed = sheet.cell(r, 1).value
            wind_temperature = sheet.cell(r, 2).value
            pressure = sheet.cell(r, 3).value
            direct_solar_rad = sheet.cell(r, 4).value
            diffuse_solar_rad = sheet.cell(r, 5).value
            total_solar_rad = sheet.cell(r, 6).value

            dataset[r - 1] = [wind_speed, wind_temperature, pressure,
                              direct_solar_rad, diffuse_solar_rad, total_solar_rad]

        return dataset
