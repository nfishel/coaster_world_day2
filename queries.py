from cs50 import SQL

# connect to the database
db = SQL("sqlite:///coasters.db")

# this function will grab all the unique countries from our database
def get_all_countries():
  rows = db.execute("""SELECT DISTINCT(country)
                    FROM coasters ORDER BY country""")
  return rows

# this function will get all the parks for a given country
def get_all_parks(country):
  query = """SELECT DISTINCT(park) FROM coasters
             WHERE country = ?"""
  # db.execute gives us a list of dictionaries
  return db.execute(query, country)


# this function will get all the coasters at a given park
def get_all_coasters(park):
  query = """SELECT id, name, year_opened FROM coasters
             WHERE park = ? ORDER BY year_opened DESC"""
  return db.execute(query, park)