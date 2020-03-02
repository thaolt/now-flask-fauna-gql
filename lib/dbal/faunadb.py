from lib.dbal import DatabaseDriver

class FaunaDBDriver(DatabaseDriver):
    def __init__(self):
        self.name = 'FaunaDB'

faunadb = FaunaDBDriver()