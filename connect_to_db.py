# A SCRIPT TO CONNECT TO THE DATABASE FOR SEEDING OR MANUAL MANIPULATION.
if __name__ == "__main__":
    from app import app
    from tournament.model import *
    connect_to_db(app)
    print("connected to the database")
    create = input("Create all tables? y/n")
    seed = input("Seed tables? y/n")
    if create.lower() == 'y':
        db.create_all()
    if seed.lower == 'y':
        # seed the tables with enough dummy rows to operate the site.
        pass