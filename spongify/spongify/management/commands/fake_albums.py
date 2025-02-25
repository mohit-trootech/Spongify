# Management Command to Generate Fake Albums

from django.core.management.base import BaseCommand
from multiprocessing import Pool
from faker import Faker
from utils.base_utils import get_model
from django.utils.timezone import now
from django.db import transaction
from requests import get
from django.core.files.base import ContentFile

Album = get_model("music", "Album")
fake = Faker()
picsum_photos = "https://picsum.photos/256/256"


def create_album(artist):
    with transaction.atomic():
        try:
            image = get(picsum_photos).content
            with open("default.jpg", "wb") as f:
                f.write(image)
            album = Album(
                name=fake.word(),
                artist=artist,
                release_date=now(),
                cover_art=ContentFile(
                    name="default.jpg", content=open("default.jpg", "rb").read()
                ),
            )
            album.save()
        except Exception:
            pass


class Command(BaseCommand):
    help = "Create Fake Album Data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, nargs="?", default=1)

    def handle(self, *args, **options):
        try:
            artists = list(get_model("music", "Artist").objects.all())
            if not artists:
                self.stdout.write(self.style.ERROR("No artists found."))
                return
            with Pool(processes=8) as pool:
                pool.map(create_album, artists * (options["count"] // len(artists) + 1))
            self.stdout.write(self.style.SUCCESS("Albums Created Successfully"))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f"Unknown Exception Occured: {err}"))
