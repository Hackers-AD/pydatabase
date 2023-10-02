from pydatabase import DatabaseManage
import inspect

class IntegerField:
    def __init__(self, null=False, blank=False, default=0, help_text="Integer Field", primary=False,
                 autoincrement=False):
        self.null = null
        self.blank = blank
        self.default = default
        self.help_text = help_text
        self.primary = primary
        self.autoincrement = autoincrement

    def __str__(self):
        type = 'INTEGER '
        null = 'NOT NULL ' if not self.null else ''
        default = f'DEFAULT {self.default} '
        primary = 'PRIMARY KEY ' if self.primary else ''
        autoincrement = 'AUTOINCREMENT ' if self.autoincrement else ''
        return (type + null + default + primary + autoincrement).rstrip()

class BooleanField:
    def __init__(self, null=False, blank=False, default=0, help_text="Boolean Field",):
        self.null = null
        self.blank = blank
        self.default = default
        self.help_text = help_text

    def __str__(self):
        type = 'INTEGER '
        null = 'NOT NULL ' if not self.null else ''
        default = f'DEFAULT {self.default} '
        return (type + null + default).rstrip()

class ImageField:
    def __init__(self, null=False, blank=False, help_text="Image Field", upload_to='/'):
        self.null = null
        self.blank = blank
        self.help_text = help_text
        self.upload_to = upload_to

    def __str__(self):
        type = f"VARCHAR(255) "
        null = "NOT NULL " if not self.null else ''
        upload_to = f"DEFAULT '{self.upload_to}'"
        return (type + null + upload_to)

class CharField:
    def __init__(self, null=False, blank=False, default='', help_text="Char Field", max_length=100):
        self.null = null
        self.blank = blank
        self.default = default
        self.help_text = help_text
        self.max_length = max_length

    def __str__(self):
        type = f'VARCHAR({self.max_length}) '
        null = 'NOT NULL ' if not self.null else ''
        default = f"DEFAULT '{self.default}'"
        return (type + null + default)

class DateTimeField:
    def __init__(self, null=False, blank=False, auto_now_add=True, help_text="DateTime Field"):
        self.null = null
        self.blank = blank
        self.help_text = help_text
        self.auto_now_add = auto_now_add

    def __str__(self):
        type = "DATETIME "
        null = 'NOT NULL ' if not self.null else ''
        default = f"DEFAULT CURRENT_TIMESTAMP " if self.auto_now_add else ''
        return (type + null + default)

class EmailField:
    def __init__(self, null=False, blank=False, default=None, help_text="Integer Field", primary=False,
                 autoincrement=False):
        self.null = null
        self.blank = blank
        self.default = default
        self.help_text = help_text

    def __str__(self):
        type = f'VARCHAR(100) '
        null = 'NOT NULL ' if not self.null else ''
        default = f"DEFAULT '{self.default}'" if self.default else ''
        return (type + null + default)

class Model:
    def __init__(self, *args, **kwargs):
        attrs = [var for var in super().__dir__() if not var.startswith('__')]
        for k,v in kwargs.items():
            if k in attrs:
                self.__setattr__(k, v)
            else:
                raise Exception("No such variable in the class")
        self.db = DatabaseManage()
        self.table = self.__class__.__name__

    def all(self):
        rows = self.db.getall(self.table)
        return rows

    def save(self):
        data = {k:v for k,v in self.__dict__.items() if k != 'db' and k !='table'}
        self.db.insert(self.table, data)

    def filter(self, **kwargs):
        print(kwargs)
        pass
