import logging
import requests
import subprocess


def main():
    file = "links.txt"
    links = get_links(file)
    for link in links:
        download_data(link)


def get_links(files):
    with open(file, "r") as file:
        data = file.read()

    return data.split()


def download_data(url):
    command = url.split()
    command.insert(0, "wget")
    r = subprocess.Popen(command, shell=True)
    r.communicate()


if __name__ == "__main__":
    main()
