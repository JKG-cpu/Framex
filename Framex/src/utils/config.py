WINDOW_SIZE = (750, 500)

def change_window_size(new_size: tuple[int, int]) -> None:
    if not isinstance(new_size, tuple):
        raise ValueError("New window size must be tuple[int, int].")

    global WINDOW_SIZE

    WINDOW_SIZE = new_size
