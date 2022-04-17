PERMISSION_OWNER = 1
PERMISSION_ADMIN = 2
PERMISSION_MOD = 3

INVITE_DEFAULT = 0
INVITE_ACCEPT = 1
INVITE_REJECT = 2


def row_dict(row):
    return {column: str(getattr(row, column))
            for column in row.__table__.c.keys()}


def rows_dict(rows):
    return [row_dict(row) for row in rows]
