from src.exceptions.exception_service import ServiceException

class FunctionCall:
    def __init__(self, function, *params):
        self.__function = function
        self.__params = params

    def call(self):
        # () - call operator in Python
        self.__function(*self.__params)

class Operation:
    def __init__(self, function_undo: FunctionCall, function_redo: FunctionCall):
        self.__function_undo = function_undo
        self.__function_redo = function_redo
        self.cascading_operations = []  # List to store cascaded undo/redo operations

    def add_cascade(self, undo_action, redo_action):
        """
        Adds a cascading undo/redo pair to this operation.
        """
        self.cascading_operations.append((undo_action, redo_action))

    def undo(self):
        # Call the primary undo function
        self.__function_undo.call()

        # Call cascading undo actions in reverse order
        for undo, _ in reversed(self.cascading_operations):
            undo.call()

    def redo(self):
        # Call the primary redo function
        self.__function_redo.call()

        # Call cascading redo actions in the order they were added
        for _, redo in self.cascading_operations:
            redo.call()


class UndoService:
    def __init__(self):
        self.__history = []
        self.__index = 0

    def record(self, operation: Operation):
        self.__history.append(operation)
        self.__index = len(self.__history)

    def undo(self) -> None:
        if self.__index == 0:
            raise ServiceException("No operations to undo!\n")
        self.__index -= 1
        self.__history[self.__index].undo()

    def redo(self) -> None:
        if self.__index == len(self.__history):
            raise ServiceException("No operations to redo!\n")
        self.__history[self.__index].redo()
        self.__index += 1

    def get_history(self):
        """
        Returns the current history for testing purposes.
        """
        return self.__history

    def get_index(self):
        """
        Returns the current index for testing purposes.
        """
        return self.__index