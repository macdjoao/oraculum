# select_all (nenhuma race cadastrado)
# select_one (race nao encontrado; payload incompleto)
# insert (payload incompleto; race ja cadastrado)
# delete (payload incompleto; race nao encontrado)
# update (payload incompleto; race nao encontrado; race ja cadastrada)


class RaceSelectAllError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: No Race record found'
        self.type = 'ErrorType: Repositories/Race/RaceSelectAllError'


class RaceNotFoundError(Exception):
    def __init__(self, race: str) -> None:
        super().__init__()
        self.race = race
        self.message = f'Error: Race {self.race} not found'
        self.type = 'ErrorType: Repositories/Race/RaceNotFoundError'
