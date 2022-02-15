import subprocess
from pathlib import Path

def main():
    dir = Path('sequences')
    for file in dir.rglob('*.fastq.gz'):
        print(file)
        execute_trimmomatic(file)
        
        
def execute_trimmomatic(file):
    command = f"java -jar /mnt/d/Trimmomatic-0.39/trimmomatic-0.39.jar SE -phred33 {file} {file} ILLUMINACLIP:adapters/TruSeq3-SE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
    command = command.split()
    print(command)
    r = subprocess.Popen(command)
    r.communicate()
    
    
if __name__ == '__main__':
    main()
