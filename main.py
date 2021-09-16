import psycopg2
import xlrd

bookName = input("Введите название населенного пункта: ")

book = xlrd.open_workbook("D:/Work/RenewableEnergy/solarRad.xlsx")
sheet = book.sheet_by_name(bookName)

database = psycopg2.connect(database="postgres", user="postgres", password="password", host="localhost", port="5432")

cursor = database.cursor()

query = """INSERT INTO weather_characteristics (locality, hour_number, wind_speed, wind_temperature,
                                                pressure, direct_solar_rad, diffuse_solar_rad, total_solar_rad) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    locality = 'Baikalsk'
    hourNumber = sheet.cell(r, 0).value
    windSpeed = sheet.cell(r, 1).value
    windTemperature = sheet.cell(r, 2).value
    pressure = sheet.cell(r, 3).value
    directSolarRad = sheet.cell(r, 4).value
    diffuseSolarRad = sheet.cell(r, 5).value
    totalSolarRad = sheet.cell(r, 6).value

    values = (locality, hourNumber, windSpeed, windTemperature,
              pressure, directSolarRad, diffuseSolarRad, totalSolarRad)

    cursor.execute(query, values)

cursor.close()
database.commit()
database.close()

print("")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported Excel into postgreSQL")
