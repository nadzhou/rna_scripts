import subprocess
from pathlib import Path


def main():
    dir = Path('/mnt/d/testing_trimomatic')
    for file in dir.rglob('*.fq.gz'):
        print(file)
        execute_fastqc(file)


def execute_fastqc(file):
    command = f"fastqc {file}"
    command = command.split()
    print(command)
    r = subprocess.Popen(command)
    r.communicate()


if __name__ == '__main__':
    main()
