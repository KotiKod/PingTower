import asyncio
from django.urls import path
from App.BackEnd.Controllers.Controllers import Controller
from App.BackEnd.Router.Router import Router
from App.BackEnd.database.Repository.RepositorySQLite.UserRepository import UserRepository
from App.BackEnd.database.Repository.RepositorySQLite.WebsiteRepository import WebsiteRepository
from App.BackEnd.database.databases.SQLite import SQLite
from App.BackEnd.Models.Website import Website


def main():
    db = SQLite("data.db")
    db.initialize_database()

    user_repo = UserRepository(db)
    wb_repo = WebsiteRepository(db)

    website_router = Router(wb_repo)

    website = Website(
        id=1,
        url="https://www.google.com/",
        user_id=2,
        status_http=True,
        dns_check=True,
        ssl_check=True,
        ep_check=True,
        loading_check=True,
        validation=True,
        time_period=300
    )
    wb_repo.create(website)

    controller = Controller(wb_repo, website)
    result = controller.websiteChecking()
    print(result)

    # urlpatterns = [
    #     path('api/websites/', website_router.as_view(), name='website-router')
    #     # другие пути...
    # ]

    # from django.core.management import execute_from_command_line
    # execute_from_command_line(['manage.py', 'runserver'])

    # website2 = wb_repo.get_websites(2)
    # print(website2)

    db.close()


if __name__ == "__main__":
    main()
