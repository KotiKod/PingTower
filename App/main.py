import asyncio
from django.urls import path
from App.BackEnd.Controllers.Controllers import Controller
from App.BackEnd.Router.Router import Router
from App.BackEnd.database.Repository.RepositorySQLite.UserRepository import UserRepository
from App.BackEnd.database.Repository.RepositorySQLite.WebsiteRepository import WebsiteRepository
from App.BackEnd.database.databases.SQLite import SQLite


def main():
    db = SQLite("data.db")
    db.initialize_database()

    user_repo = UserRepository(db)
    wb_repo = WebsiteRepository(db)

    website_router = Router(wb_repo)


    controller = Controller()

    urlpatterns = [
        path('api/websites/', website_router.as_view(), name='website-router'),
        # другие пути...
    ]

    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'runserver'])

    db.close()


if __name__ == "__main__":
    main()
