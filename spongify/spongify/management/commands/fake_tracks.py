# Generate Fake Tracks

from django.core.management.base import BaseCommand
from multiprocessing import Pool
from faker import Faker
from utils.base_utils import get_model
from django.db import transaction
from django.core.files.base import ContentFile

Track = get_model("music", "Track")
Album = get_model("music", "Album")
Artist = get_model("music", "Artist")
fake = Faker()


def create_track(album):
    with transaction.atomic():
        try:
            artists = list(Artist.objects.all())
            if not artists:
                return
            artist = artists[fake.random_int(0, len(artists) - 1)]
            track = Track(
                title=fake.word(),
                album=album,
                file=ContentFile(
                    open("cradles.mp3", "rb").read(),
                    f"{fake.word()}.mp3",
                ),
                genre=fake.random_element(
                    [
                        "pop",
                        "rock",
                        "hip_hop",
                        "electronic",
                        "jazz",
                        "classical",
                        "country",
                        "r_n_b",
                        "reggae",
                        "folk",
                        "blues",
                        "metal",
                        "punk",
                        "alternative",
                        "indie",
                        "other",
                    ]
                ),
            )
            track.save()
            track.artists.add(artist)
            track.save()
        except Exception as err:
            print(err)


class Command(BaseCommand):
    help = "Create Fake Track Data"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, nargs="?", default=1)

    def handle(self, *args, **options):
        try:
            albums = list(Album.objects.all())
            if not albums:
                self.stdout.write(self.style.ERROR("No albums found."))
                return
            with Pool(processes=8) as pool:
                pool.map(create_track, albums * (options["count"] // len(albums) + 1))
            self.stdout.write(self.style.SUCCESS("Tracks Created Successfully"))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f"Unknown Exception Occured: {err}"))
