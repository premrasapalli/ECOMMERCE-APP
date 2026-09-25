import sqlite3


# WHY:
# Database file name ను ఒక placeలో maintain చేయడానికి variable use చేస్తున్నాం.
# Later database location మార్చాలంటే ఒకే placeలో change చేయవచ్చు.
DATABASE_NAME = "ecommerce.db"


def get_db_connection():

    # WHY:
    # SQLite databaseకి connection create చేస్తున్నాం.
    # Database file లేకపోతే SQLite automatically create చేస్తుంది.
    connection = sqlite3.connect(DATABASE_NAME)

    # WHY:
    # Database rows ను dictionary-like formatలో access చేయడానికి.
    #
    # Example:
    # product["name"]
    #
    # ఇలా ఉపయోగించవచ్చు.
    connection.row_factory = sqlite3.Row

    return connection
