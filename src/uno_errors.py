
class UnoError(Exception):
    ...


class CardNotFound(UnoError):
    ...


class PlayerNotFound(UnoError):
    ...


class PondOverflow(UnoError):
    ...


class IncorrectCard(UnoError):
    ...


class InvalidWildColour(IncorrectCard):
    ...
