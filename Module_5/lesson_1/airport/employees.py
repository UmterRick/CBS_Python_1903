from datetime import datetime

from Module_5.lesson_1.airport.base_manager import BaseManager


class Employee:
    def __init__(self, obj_id, first_name, last_name, birth_date, role: str):
        self.id = obj_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.role = role

    def __repr__(self):
        return f"{self.role.title()}(id={self.id}, name={self.first_name} {self.last_name})"

    def __str__(self):
        return f"{self.role.title()}(id={self.id}, name={self.first_name} {self.last_name})"


class EmployeeManager(BaseManager):

    def create(self, first_name: str, last_name: str, birth_date: datetime.date, role: str) -> int:
        query = """
        INSERT INTO employees (first_name, last_name, birth_date, role) VALUES (%s, %s, %s, %s) RETURNING id;
        """

        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (first_name, last_name, birth_date))
                new_obj_id = cursor.fetchone()[0]
                conn.commit()
                print(f"{self.__class__.__name__} - CREATE NEW Passenger WITH ID={new_obj_id}")
                return new_obj_id

    def get_by_id(self, obj_id: int):
        query = "SELECT * FROM employees WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))
                return Employee(*cursor.fetchone())

    def delete_by_id(self, obj_id: int):
        query = "DELETE FROM employees WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))
