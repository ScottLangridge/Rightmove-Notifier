import logging

from notifier import Notifier
from rightmove_parser import RightmoveParser
from scraper import Scraper
from secrets import Secrets

targets = Secrets.TARGETS

scraper = Scraper(targets)
parser = RightmoveParser()
notifier = Notifier(Secrets.PUSHOVER_USER_KEY, Secrets.PUSHOVER_API_KEY)


def main():
    logging.basicConfig(level=logging.DEBUG, filename='RightmoveInstantNotifer.log',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('RIGHTMOVE INSTANT NOTIFIER STARTED')
    last_properties = fetch_properties()
    notifier.send_msg("RightMove Notifier Started")

    while True:
        # Update properties
        current_properties = fetch_properties()
        new_properties = list(set(current_properties) - set(last_properties))
        last_properties = current_properties

        # Notify of additions
        if new_properties:
            msg = ''
            for new_property in new_properties:
                pid = new_property.split('-')[1]
                msg += 'https://www.rightmove.co.uk/properties/' + pid + '\n'
            notifier.send_msg('New Property Alert', msg)


def fetch_properties():
    raw_pages = scraper.fetch_pages()
    properties = []
    for page in raw_pages:
        properties.extend(parser.get_flats(page))
    return properties


main()
