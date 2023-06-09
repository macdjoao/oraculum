class GradeNoRecordError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: No Grade record found'
        self.type = 'ErrorType: Repositories/Grade/RaceNoRecordError'


class GradeNotFoundError(Exception):
    def __init__(self, grade: str) -> None:
        super().__init__()
        self.grade = grade
        self.message = f'Error: Grade {self.grade} not found'
        self.type = 'ErrorType: Repositories/Grade/RaceNotFoundError'


class GradeIncompleteParamsError(Exception):
    def __init__(self, missing_param: str) -> None:
        super().__init__()
        self.missing_param = missing_param
        self.message = f'Error: Missing param "{self.missing_param}" in Grade'
        self.type = 'ErrorType: Repositories/Grade/RaceIncompleteParamsError'


class GradeAlreadyRegisteredError(Exception):
    def __init__(self, grade) -> None:
        super().__init__()
        self.grade = grade
        self.message = f'Error: Grade {self.grade} already registered'
        self.type = 'ErrorType: Repositories/Grade/RaceAlreadyRegisteredError'
