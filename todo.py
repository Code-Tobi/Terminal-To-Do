from os import system, name

class Todo():
    """ Class for a to-do list with checkbox and name """

    def __init__(self, name):
        self.name = name
        self.checkbox = False

    def __str__(self):
        checkbox = "🗹" if self.checkbox else "☐"
        return f"{self.name} {checkbox}"
    
    def toggle_checkbox(self):
        self.checkbox = not self.checkbox

class TodoList():
    """ The to-do list with functions for adding, deleting and changing the checkbox """

    def __init__(self):
        self.todos = []

    def __str__(self):
        if not self.todos:
            return "Keine To-Dos vorhanden"
        
        result = ""
        
        for index, element in enumerate(self.todos):
            result += f"({index + 1}) {element} \n"

        return result

    def _get_int(self, number):
        """ Converts string to int with security check """

        if not self.todos:
            print("Fehler! Keine To-Dos vorhanden")
            return
        
        try:
            index = int(number)
        except ValueError:
            print("Fehler! Bitte keine Buchstaben um die To-Do auszuwählen")
            return
        
        if index > len(self.todos) or index < 1:
            print("Fehler! Diese To-Do ist nicht vorhanden") 
            return

        return index

    def add(self, name):
        """ Adds a to-do """

        self.todos.append(Todo(name))

    def delete(self, number):
        """ Deletes a to-do """

        index = self._get_int(number)

        if index is None:
            return

        del self.todos[index - 1]

    def checkbox(self, number):
        """ Changes the status of the checkbox """

        index = self._get_int(number)

        if index is None:
            return

        self.todos[index - 1].toggle_checkbox()

if __name__ == "__main__":
    todos = TodoList()

    while True:
        print("--- Terminal To-Do --- \n")
        print(todos, end="\n")

        user_input = input("Was möchtest du machen: ")
        commands = user_input.split(" ", 1)
        system("cls" if name == "nt" else "clear")

        if len(commands) == 2:
            match commands[0]:
                case "add":
                    todos.add(commands[1])
                case "delete":
                    todos.delete(commands[1])
                case "checkbox":
                    todos.checkbox(commands[1])
                case _:
                    print("Fehler! Unbekannter Befehl")
        else:
            print("Fehler! Bitte gib einen Befehl mit Argument ein")