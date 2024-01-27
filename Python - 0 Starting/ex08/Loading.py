import time
import os


def get_terminal_width():
    """
    Get the width of the terminal
    """
    try:
        return os.get_terminal_size(0).columns
    except OSError:
        try:
            return int(os.environ.get('COLUMNS', os.environ.get('COLS'))) or 80
        except (TypeError, ValueError):
            return 80  # A common default value


def format_time(seconds):
    """
    Get MM:SS format from seconds
    """
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"


def ft_tqdm(lst):
    """
    Decorate an iterable object, returning an iterator which acts exactly like
    the original iterable, but prints a dynamically updating progressbar
    every time a value is requested.
    """
    total = len(lst)
    start_time = time.time()
    terminal_width = get_terminal_width()

    for i, item in enumerate(lst, 1):
        f_percentage = f"{((i * 100) // total):>3}%"
        f_progress = f"{i}/{total}"

        seconds_passed = time.time() - start_time
        speed = i / seconds_passed
        seconds_left = (total - i) / speed
        f_seconds_passed = format_time(seconds_passed)
        f_seconds_left = format_time(seconds_left)
        f_seconds = f"[{f_seconds_passed}<{f_seconds_left}, {speed:.2f}it/s]"

        # +4 for 2 "|" and 2 spaces
        paddings = len(f_percentage) + len(f_progress) + len(f_seconds) + 4
        bar_total = terminal_width - paddings
        bar_width = i * bar_total // total
        f_bar = f"{'█' * bar_width:<{bar_total}}"
        print(f"\r{f_percentage}|{f_bar}| {f_progress} {f_seconds}", end="",
              flush=True)
        yield item
