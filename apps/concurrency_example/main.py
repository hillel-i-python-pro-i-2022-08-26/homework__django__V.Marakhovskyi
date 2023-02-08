from concurrent.futures import ThreadPoolExecutor


def my_action(numbeer: int) -> int:
    return numbeer**2


def make_with_classic_way(items: list[int]) -> list[int]:
    return [my_action(item) for item in items]


def make_with_thread_pool_executor(items: list[int]) -> list[int]:
    with ThreadPoolExecutor() as executor:
        results = executor.map(my_action, items)

    return list[results]


def main():
    items = list(range(10))
    make_with_classic_way(items)
    make_with_thread_pool_executor(items)


if __name__ == "__main__":
    my_action()
