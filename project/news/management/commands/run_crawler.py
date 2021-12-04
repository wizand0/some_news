from django.core.management.base import BaseCommand
from news.crawlers.bbc_crawler import crawl_one


class Command(BaseCommand):
    help = 'Run BBC News crawler'

    def handle(self, *args, **options):
        url = 'https://4pda.to/2021/12/04/393919/minusy_sovremennykh_smartfonov_igra_v_kalmara_v_realnoj_zhizni_glavnoe_za_nedelyu/'
        crawl_one(url)
