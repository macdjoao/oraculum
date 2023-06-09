# insert (race ja cadastrado)
# update (race ja cadastrada)


class RaceNoRecordError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: No Race record found'
        self.type = 'ErrorType: Repositories/Race/RaceNoRecordError'


class RaceNotFoundError(Exception):
    def __init__(self, race: str) -> None:
        super().__init__()
        self.race = race
        self.message = f'Error: Race {self.race} not found'
        self.type = 'ErrorType: Repositories/Race/RaceNotFoundError'


class RaceIncompleteParamsError(Exception):
    def __init__(self, missing_param: str) -> None:
        super().__init__()
        self.missing_param = missing_param
        self.message = f'Error: Missing param "{self.missing_param}" in Race'
        self.type = 'ErrorType: Repositories/Race/RaceIncompleteParamsError'


class RaceAlreadyRegisteredError(Exception):
    def __init__(self, race) -> None:
        super().__init__()
        self.race = race
        self.message = f'Error: Race {self.race} already registered'
        self.type = 'ErrorType: Repositories/Race/RaceAlreadyRegisteredError'
