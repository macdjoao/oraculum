# insert (raça/classe nao encontrada)
# update_level (level invalido)
# update_race (raça nao encontrada)
# update_grade (classe nao encontrada)


class PlayerNoRecordError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: No Player record found'
        self.type = 'ErrorType: Repositories/Player/PlayerNoRecordError'


class PlayerNotFoundError(Exception):
    def __init__(self, player: str) -> None:
        super().__init__()
        self.player = player
        self.message = f'Error: Player {self.player} not found'
        self.type = 'ErrorType: Repositories/Player/PlayerNotFoundError'


class PlayerIncompleteParamsError(Exception):
    def __init__(self, missing_param: str) -> None:
        super().__init__()
        self.missing_param = missing_param
        self.message = f'Error: Missing param "{self.missing_param}" in Player'
        self.type = (
            'ErrorType: Repositories/Player/PlayerIncompleteParamsError'
        )


class PlayerAlreadyRegisteredError(Exception):
    def __init__(self, player) -> None:
        super().__init__()
        self.player = player
        self.message = f'Error: Player {self.player} already registered'
        self.type = (
            'ErrorType: Repositories/Player/PlayerAlreadyRegisteredError'
        )


class PlayerLevelNotIntError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = f'Error: Param "level" is not a integer'
        self.type = 'ErrorType: Repositories/Player/PlayerLevelNotIntError'
