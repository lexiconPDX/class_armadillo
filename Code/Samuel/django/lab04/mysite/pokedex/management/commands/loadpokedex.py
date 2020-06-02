from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, Type
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data)
        pass