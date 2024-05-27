class KeyboardController:
    def __init__(self,
                 up: str,
                 down: str,
                 left: str,
                 right: str,
                 shoot: str,
                 ):
        self.up = up

    def handle_button(self, user_input):
        match user_input:
            case self.up:
                ...


class BasePlayer:
    def __init__(self, control_data):
        self.control_handler = KeyboardController(**control_data)

    def control(self):
        raise NotImplementedError


class Player1(BasePlayer):


    def control(self):
        return "forward"


class Player2(BasePlayer):
    ...



player_1 = Player1(control_data={"up": "w", "down": "s"})
player_2 = Player1(control_data={"up": "arrow_up", "down": "arrow_down"})