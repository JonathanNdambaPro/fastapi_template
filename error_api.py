class LowerCaseError(ValueError):
    def __init__(self, value):
        message = f"{value} Not in lower case"
        super().__init__(message)

class GreaterThanFourNumber(ValueError):
    ...

class DateMatchingError(ValueError):
    ...