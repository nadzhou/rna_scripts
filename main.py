import logging
from scripts.download_file import get_links
from scripts.download_file import download_data
from scripts.execute_fastqc import execute_fastqc

from pathlib import Path

def main():
    file = "links.txt"
    dir = Path('/mnt/d/testing_trimomatic')


    logging.info("Fetching download links...")
    links = get_links(file)
    logging.info("Starting download...")
    for link in links:
        out = download_data(link)
        logging.info(out)
        logging.info(f"{link} downloaded.")
    logging.info('Files downloaded.')

    logging.info('Initiating FASTQC...')

    for file in dir.rglob('*.fq.gz'):
        out = execute_fastqc(file)
        logging.info(out)
        logging.info(f"{file} analysis done.")


if __name__ == '__main__':
    main()
