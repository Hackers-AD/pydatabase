import sqlite3

class DatabaseManage:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, attr):
        params = []
        for col, dtype in attr.items():
            params.append(col + " " + dtype.__str__())
        query = f"CREATE TABLE {table_name}({', '.join(params)})"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            print(f"Table {table_name} created successfully!")
        except Exception as error:
            print(str(error).capitalize())
    def getall(self, table):
        query = f"SELECT * FROM {table}"
        rows = self.cursor.execute(query).fetchall()
        return rows

    def insert(self, table, data):
        query = f"INSERT INTO {table} ({','.join(data.keys())}) VALUES ({','.join(['?'] * len(data))})"
        try:
            self.cursor.execute(query, tuple(data.values()))
            self.conn.commit()
            print(f"Data added to table {table}")
        except Exception as error:
            print(error)

if __name__ == "__main__":
    dbmanager = DatabaseManage()
    dbmanager.create_table("Person", {id: 0})
