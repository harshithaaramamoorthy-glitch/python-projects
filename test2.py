import mysql.connector

# ✅ Database configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PORT = 3306
DB_PASSWORD = "harshithaa@99"
DB_NAME = "employeedb"


def get_connection():
    """Establish a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as e:
        print("Couldn't connect to MySQL.")
        print("Error:", e)
        return None


def create_student():
    """Prompt the user for student info and insert into the database."""
    name = input("Enter student name: ").strip()
    age_text = input("Enter age (number): ").strip()

    if not name or not age_text.isdigit():
        print("Please provide a valid name and a number for age.")
        return

    age = int(age_text)

    conn = get_connection()
    if not conn:
        return

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO student (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        print("✅ Student added successfully!")
    except mysql.connector.Error as e:
         print("Error inserting student:", e)
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    create_student()
