from time import time,sleep
from threading import Thread
def download(file):
    print(f"Downloading {file}....")
    sleep(0.5)
    print("Download Complete.")
if __name__=="__main__":
    files=["video.mp4","img.png","audio.mp4"]
    start=time()
    for f in files:
        download(f)
    end=time()
    print(f"Without thread time difference: {end-start:.2f}")

    threads=[]
    for f in files:
        t= Thread(target=download,args=(f,))
        threads.append(t)
    start=time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end=time()
    print(f"With thread time difference {end-start:.2f}")