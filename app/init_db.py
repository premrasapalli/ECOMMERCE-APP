from database import get_db_connection


# WHY:
# Database మరియు products table create చేయడానికి
# ఈ function ఉపయోగిస్తున్నాం.
def create_database():

    # WHY:
    # SQLite databaseకి connection తీసుకుంటున్నాం.
    connection = get_db_connection()

    # WHY:
    # Products information store చేయడానికి products table అవసరం.
    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    # WHY:
    # CREATE TABLE operation databaseలో permanently save చేయడానికి.
    connection.commit()

    # WHY:
    # Database connection close చేయాలి.
    # Unnecessary open connections avoid చేయడానికి.
    connection.close()

    print("Database initialized successfully.")


# WHY:
# ఈ file directగా run చేసినప్పుడు
# create_database() function execute అవుతుంది.
if __name__ == "__main__":
    create_database()
