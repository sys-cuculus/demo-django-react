from enum import Enum

class Status(Enum):
    UNASIGNED = 1
    ASSIGNED = 2
    WORKING = 3
    REVIEW = 4
    CLOSED = 5


class Proirity(Enum):
    URGENT = 1
    CARRENT = 2
    CAN_WAIT = 3
    LATER = 4
