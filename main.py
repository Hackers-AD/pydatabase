import argparse
import schema
import inspect
import re
from pydatabase import DatabaseManage

parser = argparse.ArgumentParser(description="Manage database model using CLI.")
parser.add_argument('migrate', help="Migrate the database")

args = parser.parse_args()

dbmanager = DatabaseManage()
if args.migrate == "migrate":
    schemas = [name for name, obj in inspect.getmembers(schema, inspect.isclass)]
    regex = re.compile(r'__[a-z]+__')
    for table in schemas:
        attr = {}
        for k, v in schema.__dict__[table].__dict__.items():
            if not re.match(regex, k):
                attr[k] = v
        dbmanager.create_table(table, attr)
