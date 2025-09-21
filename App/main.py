import asyncio

from App.BackEnd.Controllers.Controllers import Controller
from App.BackEnd.database.Repository.RepositorySQLite.UserRepository import UserRepository
from App.BackEnd.database.Repository.RepositorySQLite.WebsiteRepository import WebsiteRepository
from App.BackEnd.database.databases.SQLite import SQLite


def main():
    db = SQLite("data.db")
    db.initialize_database()

    user_repo = UserRepository(db)
    wb_repo = WebsiteRepository(db)

    controller = Controller()

    db.close()


if __name__ == "__main__":
    main()
