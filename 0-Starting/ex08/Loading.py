import time
from time import sleep
import shutil


def get_format_time(sec):
    """Take seconds and return minutes:seconds"""
    min = sec / 60
    sec = sec % 60
    return f"{int(min):02d}:{int(sec):02d}"


def ft_tqdm(lst: range) -> None:
    """Take a range and print the progress bar of it."""
    total = len(lst)
    start_time = time.time()
    width = max(shutil.get_terminal_size().columns - 40, 5)
    for i, item in enumerate(lst, 1):
        curr_time = time.time() - start_time
        speed = i / curr_time
        size = int(i / total * width)
        percent = int(i / total * 100)

        curr_time_str = get_format_time(curr_time)
        eta = get_format_time((total - i) / speed)

        progress = f"{percent}%|{'█' * size:<{width}}| {i}/{total}"
        inf_time = f"[{curr_time_str}<{eta}, {speed:.2f}it/s]"

        print(f"\r{progress} {inf_time}", end="", flush=True)
        yield item


def main():
    for elem in ft_tqdm(range(100)):
        sleep(0.001)


if __name__ == "__main__":
    main()
