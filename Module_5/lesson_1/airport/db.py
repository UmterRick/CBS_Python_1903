import psycopg2

create_passengers_table = """
 CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE
)
"""

create_tickets_type = """
 DROP TYPE IF EXISTS ticket_type ;
 CREATE TYPE ticket_type as ENUM('economy', 'business', 'first', 'second');
"""

create_tickets_table = """

 CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    passenger_id INT NOT NULL DEFAULT -1,
    flight_id INT NOT NULL,
    type ticket_type,
    luggage BOOL DEFAULT FALSE,
    FOREIGN KEY (passenger_id) REFERENCES passengers (id) ON DELETE SET DEFAULT,
    FOREIGN KEY (flight_id) REFERENCES flights (id) ON DELETE CASCADE 
    );
    
"""

create_employee_roles = """
 DROP TYPE IF EXISTS employee_type;
 CREATE TYPE employee_type as ENUM('pilot', 'manager', 'stuart', 'mechanic');

"""

create_employees_table = """
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    role employee_type
)
"""

create_planes_table = """
    CREATE TABLE IF NOT EXISTS planes (
        id SERIAL PRIMARY KEY,
        model VARCHAR(255) NOT NULL,
        pilot_1 INT NOT NULL,
        pilot_2 INT,
        seats INT CHECK ( seats > 0 AND seats <= 500)   ,
        FOREIGN KEY (pilot_1) REFERENCES employees (id) ON DELETE CASCADE,
        FOREIGN KEY (pilot_2) REFERENCES employees (id) ON DELETE CASCADE 
        )
"""

create_flights_table = """
CREATE TABLE IF NOT EXISTS flights (
        id SERIAL PRIMARY KEY,
        destination VARCHAR(255) NOT NULL,
        departure VARCHAR(255) NOT NULL,
        gate INT NOT NULL,
        departure_date DATE,
        departure_time TIME,
        plane_id INT NOT NULL,
        FOREIGN KEY (plane_id) REFERENCES planes (id) ON DELETE CASCADE 
        )
"""


def init_db(conn_params):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cursor:
            print("DB INITIALIZATION ...")
            cursor.execute(create_passengers_table)
            # cursor.execute(create_tickets_type)
            # cursor.execute(create_employee_roles)
            cursor.execute(create_employees_table)
            cursor.execute(create_planes_table)
            cursor.execute(create_flights_table)
            cursor.execute(create_tickets_table)

            conn.commit()
            print("DB INITIALIZATION - COMPLETE")

