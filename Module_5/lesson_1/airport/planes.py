from Module_5.lesson_1.airport.base_manager import BaseManager
from Module_5.lesson_1.airport.employees import Employee, EmployeeManager
from Module_5.lesson_1.const import CONNECTION_PARAMS


class Plane:
    def __init__(self, obj_id, model, pilot_1, pilot_2, seats):
        self.id = obj_id
        self.model = model
        self.pilot_1 = pilot_1
        self.pilot_2 = pilot_2
        self.seats = seats

    def get_pilot_info(self, pilot_num):
        if pilot_num == 1:
            return EmployeeManager(CONNECTION_PARAMS).get_by_id(obj_id=self.pilot_1)
        elif pilot_num == 2:
            if self.pilot_2 is None:
                return None
            return EmployeeManager(CONNECTION_PARAMS).get_by_id(obj_id=self.pilot_2)


    def __repr__(self):
        return f"Plane(id={self.id}, model={self.model})"

    def __str__(self):
        return f"Plane(id={self.id}, model={self.model})"


class PlaneManager(BaseManager):

    def create(self, model: str, pilot_1: int, pilot_2: int | None, seats: int) -> int:
        query = """
        INSERT INTO planes (model, pilot_1, pilot_2, seats) VALUES (%s, %s, %s, %s) RETURNING id;
        """

        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (model, pilot_1, pilot_2, seats))
                new_plane_id = cursor.fetchone()[0]
                conn.commit()
                print(f"PlaneManager - CREATE NEW PLANE WITH ID={new_plane_id}")
                return new_plane_id

    def get_by_id(self, obj_id: int):
        query = "SELECT id, model, pilot_1, pilot_2, seats FROM planes WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))
                plane_args = cursor.fetchone()
                print(plane_args)
                return Plane(*plane_args)

    def delete_by_id(self, obj_id: int):
        query = "DELETE FROM planes WHERE id = %s;"
        with self._connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (obj_id,))
