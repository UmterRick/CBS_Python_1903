import datetime

from Module_5.lesson_1.airport.base_manager import BaseManager


class PassengerManager(BaseManager):

    def create(self, first_name: str, last_name: str, birth_date: datetime.date) -> int:
        query = """
        INSERT INTO passengers (first_name, last_name, birth_date) VALUES (%s, %s, %s) RETURNING id;
        """

        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (first_name, last_name, birth_date))
                new_obj_id = cursor.fetchone()[0]
                conn.commit()
                print(f"{self.__class__.__name__} - CREATE NEW Passenger WITH ID={new_obj_id}")
                return new_obj_id

    def get_by_id(self, obj_id: int):
        query = "SELECT * FROM passengers WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))
                return cursor.fetchone()

    def delete_by_id(self, obj_id: int):
        query = "DELETE FROM passengers WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))