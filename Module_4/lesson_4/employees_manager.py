import datetime
import sqlite3
import logging
from typing import Iterable

logger = logging.getLogger("nameOfTheLogger")
logger.addHandler(logging.StreamHandler())
logger.setLevel("DEBUG")


class EmployeesManager:
    def __init__(self):
        self.table_name = "employees"
        self.db_name = 'db4.sqlite3'

    def create(self, name: str, birth_date: datetime.date, role: str, salary: int, department: str):
        logger.info("Create conn with DB...")
        conn = sqlite3.connect(self.db_name)
        try:
            create_query = f"""
            INSERT INTO employees (name, birth_date, role, salary, department) 
            VALUES(?, ?, ?, ?, ?)
            """
            query_params = (name, birth_date, role, salary, department)
            conn.execute(create_query, query_params)
            conn.commit()
            logger.info(f"New Employee(name={name}) was SUCCESSFULLY added!")

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
        finally:
            logger.info("Close connection to DB!")
            conn.close()

    def get_all(self) -> list:
        logger.info("Create conn with DB ...")
        conn = sqlite3.connect('db4.sqlite3')
        try:
            query = f"""
                    SELECT * FROM employees
                    """
            cursor = conn.cursor()
            cursor.execute(query)
            employee_data = cursor.fetchall()
            return employee_data

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
            return []
        finally:
            logger.info("Close connection to DB!")
            conn.close()

    def update_name(self, new_name: str, employee_id: int):
        logger.info("Create conn with DB ...")
        conn = sqlite3.connect('db4.sqlite3')
        try:
            query = f"""
                            UPDATE employees SET name=? WHERE id=?
                            """
            conn.execute(query, (new_name, employee_id))
            conn.commit()
            logger.info(f"New name for Employee(id={employee_id}) was SUCCESSFULLY updated!")

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
            return []
        finally:
            logger.info("Close connection to DB!")
            conn.close()

    def create_many(self, new_employees_data: tuple):
        logger.info("Create conn with DB...")
        conn = sqlite3.connect(self.db_name)
        try:
            create_query = f"""
                   INSERT INTO employees (name, birth_date, role, salary, department) 
                   VALUES(?, ?, ?, ?, ?)
                   """
            conn.executemany(create_query, new_employees_data)
            conn.commit()

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
        finally:
            logger.info("Close connection to DB!")
            conn.close()


    def delete_by_id(self, employee_id):
        logger.info("Create conn with DB ...")
        conn = sqlite3.connect('db4.sqlite3')
        try:
            query = f""" DELETE FROM employees WHERE id=?"""
            conn.execute(query, (employee_id, ))
            conn.commit()
            logger.info(f"Employee(id={employee_id}) was SUCCESSFULLY deleted!")

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
            return []
        finally:
            logger.info("Close connection to DB!")
            conn.close()

    def delete_many_by_ids(self, employee_ids: Iterable):
        logger.info("Create conn with DB ...")
        conn = sqlite3.connect('db4.sqlite3')
        prepare_params = [(obj_id, ) for obj_id in employee_ids]
        try:
            query = f""" DELETE FROM employees WHERE id=?"""
            conn.executemany(query, prepare_params)
            conn.commit()

        except sqlite3.DatabaseError as exc:
            logger.error(f"Error while executing query: {exc}")
            return []
        finally:
            logger.info("Close connection to DB!")
            conn.close()




data_manager = EmployeesManager()
# EmployeesManager().create(
#     name="DELETE FROM employees WHERE 1=1",  # SQL Injection
#     birth_date=datetime.date(2000, 1, 1),
#     role="cleaner",
#     salary=1000,
#     department="IT",
# )

# data = data_manager.get_all()
# print(data)
# data_manager.update_name("Jack Jonson", 1)
# data = data_manager.get_all()
# print(data)

new_data_collection = (
    ("Employee 1", datetime.date(2000, 1, 1), "Software Engineer", 10000, "IT"),
    ("Employee 2", datetime.date(2000, 1, 2), "Software Engineer", 11000, "IT"),
    ("Employee 3", datetime.date(2000, 1, 3), "Software Engineer", 12000, "IT"),
    ("Employee 4", datetime.date(2000, 1, 4), "Software Engineer", 13000, "IT"),
    ("Employee 5", datetime.date(2000, 1, 5), "Software Engineer", 14000, "IT"),
)

# data_manager.create_many(new_data_collection)
# data_manager.delete_by_id(2)
# data_manager.delete_many_by_ids((1, 3, 5)) # -> ( (1), (3), (5) )

data_manager.delete_many_by_ids([1, 2, 3, 4, 5])