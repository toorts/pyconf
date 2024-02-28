import os
import random

import django
from django.contrib.auth.models import Group, Permission
from main.models import Author, Paper, User, Reviewer, Chair, Conference

from faker import Faker, factory


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conferencesystem.settings')
django.setup()

fake = Faker()


def create_users(N) -> None:
    for _ in range(N):
        username = fake.user_name()
        email = fake.email()
        password = "author"
        User(email=email, password=password, type="author").save()
        Author(name=username, email=email, password=password).save()


def create_chairs(N) -> None:
    for _ in range(N):
        username = fake.user_name()
        email = fake.email()
        password = "chair"
        User(email=email, password=password, type="chair").save()
        Chair(name=username, email=email,
              password=password, is_accepted=True).save()


def create_reviewers(N) -> None:
    for _ in range(N):
        username = fake.user_name()
        email = fake.email()
        password = "review"
        User(email=email, password=password, type="reviewer").save()
        Reviewer(name=username, email=email,
                 password=password, is_accepted=True).save()


if __name__ == "__main__":
    # create_reviewers(10)
    # create_chairs(5)
    # create_users(50)
    bf = BookFactory()
