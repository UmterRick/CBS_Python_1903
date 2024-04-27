class GraphicalObject:
    ...


class Rectangle(GraphicalObject):
    ...


class ClickHandler:
    def action(self):
        print("You click me!")


class Button:
    def __init__(self, shape: GraphicalObject, handler: ClickHandler):
        self.shape = shape
        self.handler = handler

    def on_click(self):
        self.handler.action()



rectangle_button = Button(shape=Rectangle(), handler=ClickHandler())
rectangle_button.on_click()




