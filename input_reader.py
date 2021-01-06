import csv
import psycopg2

con = psycopg2.connect(database="tup_seminarska", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

cursor = con.cursor()

INPUT_DATA = "input_data/"
def readFile2015():
    with open(f"{INPUT_DATA}2015.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[0]
                region  = row[1]
                happiness = row[3]
                economy = row[5]
                normalised_economy = (float(economy) - 0) / (1.69 - 0)
                family = row[6]
                normalised_family = (float(family) - 0) / (1.4 - 0)
                health = row[7]
                normalised_health = (float(health) - 0) / (1.03 - 0)
                freedom = row[8]
                normalised_freedom = (float(freedom) - 0) / (0.67 - 0)
                g_trust = freedom = row[9]
                normalised_trust = (float(g_trust) - 0) / (0.55 - 0)
                generosity = row[10]
                normalised_genero = (float(generosity) - 0) / (0.8 - 0)
                stmt = f"INSERT INTO happiness_schema.happiness (country, region, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', '{region}', {2015}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()


def readFile2016():
    with open(f"{INPUT_DATA}2016.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[0]
                region = row[1]
                happiness = row[3]
                economy = row[6]
                normalised_economy = (float(economy) - 0) / (1.82 - 0)
                family = row[7]
                normalised_family = (float(family) - 0) / (1.18 - 0)
                health = row[8]
                normalised_health = (float(health) - 0) / (0.95 - 0)
                freedom = row[9]
                normalised_freedom = (float(freedom) - 0) / (0.61 - 0)
                g_trust = row[10]
                normalised_trust = (float(g_trust) - 0) / (0.51 - 0)
                generosity = row[10]
                normalised_genero = (float(generosity) - 0) / (0.82 - 0)
                stmt = f"INSERT INTO happiness_schema.happiness (country, region, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', '{region}', {2016}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()


def readFile2017():
    with open(f"{INPUT_DATA}2017.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[0].strip('"')
                happiness = row[2]
                economy = row[5]
                normalised_economy = (float(economy) - 0) / (1.87 - 0)
                family = row[6]
                normalised_family = (float(family) - 0) / (1.61 - 0)
                health = row[7]
                normalised_health = (float(health) - 0) / (0.95 - 0)
                freedom = row[8]
                normalised_freedom = (float(freedom) - 0) / (0.66 - 0)
                g_trust = row[10]
                normalised_trust = (float(g_trust) - 0) / (0.46 - 0)
                generosity = row[9]
                normalised_genero = (float(generosity) - 0) / (0.84 - 0)
                stmt = f"INSERT INTO happiness_schema.happiness (country, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', {2017}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()


def readFile2018():
    with open(f"{INPUT_DATA}2018.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[1].strip('"')
                happiness = row[2]
                economy = row[3]
                normalised_economy = (float(economy) - 0) / (2.1 - 0)
                family = row[4]
                normalised_family = (float(family) - 0) / (1.64 - 0)
                health = row[5]
                normalised_health = (float(health) - 0) / (1.03 - 0)
                freedom = row[6]
                normalised_freedom = (float(freedom) - 0) / (0.72 - 0)
                g_trust = row[8]
                normalised_trust = g_trust
                generosity = row[7]
                normalised_genero = (float(generosity) - 0) / (0.6 - 0)
                if normalised_trust == "N/A":
                    normalised_trust = "null"
                stmt = f"INSERT INTO happiness_schema.happiness (country, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', {2018}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()


def readFile2019():
    with open(f"{INPUT_DATA}2019.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[1].strip('"')
                happiness = row[2]
                economy = row[3]
                normalised_economy = (float(economy) - 0) / (1.68 - 0)
                family = row[4]
                normalised_family = (float(family) - 0) / (1.62 - 0)
                health = row[5]
                normalised_health = (float(health) - 0) / (1.14 - 0)
                freedom = row[6]
                normalised_freedom = (float(freedom) - 0) / (0.63 - 0)
                g_trust = row[8]
                normalised_trust = g_trust
                generosity = row[7]
                normalised_genero = (float(generosity) - 0) / (0.57 - 0)
                stmt = f"INSERT INTO happiness_schema.happiness (country, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', {2019}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()


def readFile2020():
    with open(f"{INPUT_DATA}2020.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[0].strip('"')
                region = row[1].strip('"')
                happiness = row[2]
                economy = row[13]
                normalised_economy = (float(economy) - 0) / (1.54 - 0)
                family = row[14]
                normalised_family = (float(family) - 0) / (1.55 - 0)
                health = row[15]
                normalised_health = (float(health) - 0) / (1.14 - 0)
                freedom = row[16]
                normalised_freedom = (float(freedom) - 0) / (0.69 - 0)
                g_trust = row[18]
                normalised_trust = (float(g_trust) - 0) / (0.53 - 0)
                generosity = row[17]
                normalised_genero = (float(generosity) - 0) / (0.57 - 0)
                stmt = f"INSERT INTO happiness_schema.happiness (country, region, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}', '{region}', {2020}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                cursor.execute(stmt)
            i += 1
        con.commit()

def readFile2008to2015():
    with open(f"{INPUT_DATA}2008-2017_full.csv", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 1
        for row in spamreader:
            if i > 1:
                country = row[0].strip('"')
                year = int(row[1])
                try:
                    happiness = row[2]
                    economy = row[3]
                    normalised_economy = (float(economy) - 6.38) / (11.8 - 6.38)
                    family = row[4]
                    normalised_family = (float(family) - 0.29) / (0.99 - 0.29)
                    health = row[5]
                    normalised_health = (float(health) - 37.8) / (76.5 - 37.8)
                    freedom = row[6]
                    normalised_freedom = (float(freedom) - 0.26) / (0.99 - 0.26)
                    g_trust = row[8]
                    normalised_trust = 1 - (float(g_trust) - 0.04) / (0.98 - 0.04) # data is inversed -> perception of corruption
                    generosity = row[7]
                    generosity = float(generosity) + 0.32 # to up the scala from negative margin
                    normalised_genero = (float(generosity) - 0) / (0.57 + 0.32 - 0)
                    cursor.execute(f"SELECT id FROM happiness_schema.happiness WHERE country = '{country}' AND year = {year}") # check to not duplicate data
                    result = cursor.fetchone()
                    if not result:
                        stmt = f"INSERT INTO happiness_schema.happiness (country, year, economy, family, health, freedom, government_trust, happiness_score, generosity) VALUES ('{country}',{year}, {normalised_economy}, {normalised_family}, {normalised_health}, {normalised_freedom}, {normalised_trust}, {float(happiness)}, {normalised_genero})"
                        cursor.execute(stmt)
                except:
                    # if there is no data regarding values just pass row
                    # print(f"error with {country} {year}  row {i}") Couple of errors due to missing data
                    pass

            i += 1
        con.commit()

def main():
    readFile2015()
    readFile2016()
    readFile2017()
    readFile2018()
    readFile2019()
    readFile2020()
    readFile2008to2015()
    con.close()
main()
