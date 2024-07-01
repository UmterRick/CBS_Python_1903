from Module_5.lesson_1.airport.db import init_db
from Module_5.lesson_1.airport.planes import PlaneManager
from Module_5.lesson_1.const import CONNECTION_PARAMS

if __name__ == "__main__":
    init_db(conn_params=CONNECTION_PARAMS)

    plane_manager = PlaneManager(CONNECTION_PARAMS)
    # plane_manager.create("Boing", 2, None, 250)
    plane = plane_manager.get_by_id(2)
    print(plane.get_pilot_info(1))
