from django.core.management.base import BaseCommand
from news.crawlers.bbc_crawler import crawl_one


class Command(BaseCommand):
    help = 'Run BBC News crawler'

    def handle(self, *args, **options):
        url = 'https://www.techcult.ru/robots/10367-dron-s-kogtyami-yastreba'
        crawl_one(url)
