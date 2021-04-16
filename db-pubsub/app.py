import subscriber as sub
import db

def main():
    print('App Start')
    params = [
        "12345",
        "studentname",
        "studentid",
        "studentaccount"
    ]
    db.drop_table()
    db.create_db()
    sub.subscriber()

if __name__ == "__main__":
    main()
