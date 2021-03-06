import logging
import requests
import subprocess


def main():
    file = "links.txt"
    links = get_links(file)
    for link in links:
        download_data(link)


def get_links(file):
    with open(file, "r") as file:
        data = file.read()

    return data.split()


def download_data(url):
    command = url.split()
    command.insert(0, "wget")
    r = subprocess.Popen(command)
    (out, err) = r.communicate()
    return out


if __name__ == "__main__":
    main()
