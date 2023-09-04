import argparse
import requests as req
import sqlite3

def create_parser():
    _parser = argparse.ArgumentParser(
        prog= 'Bored wrapper',
        description='Create a task to ease your boredom',
    )

    _parser.add_argument(
        'run_type',
        action='store',
        help='program run type, list - show task list, new - get new task',
        choices=['list', 'new']
    )

    _parser.add_argument(
        '--type',
        dest='type',
        action='store',
        help='activity type to request',
        type=str
    )
    _parser.add_argument(
        '--key',
        dest='key',
        action='store',
        help='activity key to request',
        type=int
    )
    _parser.add_argument(
        '--participants',
        dest='participants',
        action='store',
        help='number of participants for the task',
        type=int
    )
    _parser.add_argument(
        '--price',
        dest='price',
        action='store',
        help='price for the task',
        type=float
    )
    _parser.add_argument(
        '--price_min',
        dest='price_min',
        action='store',
        help='minimum price for the task',
        type=float
    )
    _parser.add_argument(
        '--price_max',
        dest='price_max',
        action='store',
        help='maximum price for the task',
        type=float
    )
    _parser.add_argument(
        '--accessibility',
        dest='accessibility',
        action='store',
        help='accessibility value',
        type=float
    )
    _parser.add_argument(
        '--accessibility_min',
        dest='accessibility_min',
        action='store',
        help='minimum accessibility',
        type=float
    )
    _parser.add_argument(
        '--accessibility_max',
        dest='accessibility_max',
        action='store',
        help='maximum accessibility',
        type=float
    )

    return _parser

class activity_class:
    def __init__(self,
            activity = None,
            type = None,
            participants = None,
            price = None,
            link = None,
            key = None,
            accessibility = None,
    ):
        self.activity = activity
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key
        self.accessibility = accessibility

    def __str__(self):
        return f"Activity - {self.activity}, type: {self.type}, participants: {self.participants}, price: {self.price}, link: {self.link}, key: {self.key}, accessibility: {self.accessibility}"

    def __repr__(self):
        return f"<Activity {self.key}>"

    def db_format(self):
        return f'''(key, activity, type, participants, price, link, accessibility)
                VALUES ({self.key}, "{self.activity}", "{self.type}", {self.participants}, {self.price}, "{self.link}", {self.accessibility})'''

class DB_interface:
    def __init__(self, db_location):
        self._connection = sqlite3.connect(db_location)
        self._cursor = self._connection.cursor()

    def add_task(self, act: activity_class):
        self._cursor.execute(f'INSERT INTO tasks {act.db_format()}')

        self._connection.commit()

    def list(self, depth):
        res = self._cursor.execute("SELECT * FROM tasks")
        return res.fetchall()[-depth:]



def get_activity(**request_values):

    resp = req.get("http://www.boredapi.com/api/activity/", params=request_values)

    if resp.status_code != 200:
        raise Exception(f"{resp.status_code} {resp.text}")

    r_j = resp.json()

    if 'error' in r_j:
        raise Exception(r_j['error'])

    return activity_class(**r_j)

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    DB = DB_interface("tasks.db")

    try:
        if args.__dict__['run_type'] == 'new':

            task = get_activity(**args.__dict__)

            DB.add_task(task)

            print(task)
        else:
            print("\n".join(map(str, DB.list(5))))
    except Exception as e:
        print("Encountered an error:", e)