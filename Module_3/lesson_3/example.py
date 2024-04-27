import datetime

"""
private def method(self): ->  def __method(self):
    ...
    
public def method(self): ->  def method(self):
    ...
    
protected def method(self): ->  def _method(self):
    ...
"""


class Discord:
    theme: str = "Dark"
    __server_address = "102.106.934.3"
    __dev_password = "1234qwer"

    def send_message(self, message):
        self.__check_connection()
        self._connect_to_server()
        self.__play_send_message_sound()
        self.__display_new_message_in_chat(message)

    def get_address(self, password):
        if password == self.__dev_password:
            return self.__server_address
        print("You are not allowed to get server address")

    def set_address(self, new_address):
        # a lot of validation ...
        #
        self.__server_address = new_address


    def __check_connection(self):
        print("Connect to Internet")

    def _connect_to_server(self):
        print(f"Go to Discord Server at {self.__server_address}")

    def __play_send_message_sound(self):
        print("Beep")

    def __display_new_message_in_chat(self, message):
        print(f"User: {message} {datetime.datetime.now().time()}")


discord = Discord()
discord.send_message("Hello!")
# discord._connect_to_server()
# discord.__server_address = "sakdasmdaskmdaskl"
# discord._connect_to_server()
print("--------------")
discord._Discord__play_send_message_sound()
