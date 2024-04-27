class Editor:

    def __init__(self, document):
        self.document = document

    def view_doc(self):
        print(self.document)

    def edit_doc(self, new_document=None):
        print("Method not allows in free version of Editor")


class ProEditor(Editor):
    def edit_doc(self, new_document=None):
        if new_document is not None:
            self.document = new_document


licence_key = "qwer1234"
user_key = input("Provide licence key: ")
user_document = input("Document: ")

if user_key == licence_key:
    editor = ProEditor(user_document)
else:
    editor = Editor(user_document)

editor.view_doc()

editor.edit_doc("New Doc")

editor.view_doc()




