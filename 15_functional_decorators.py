from typing import Callable, Any


def number_filter(func: Any) -> Any:
    def wrapper(data: Any) -> Any:
        items = [x for x in data if isinstance(x, (int, float))]
        return func(items)

    return wrapper


def round_dict(func: Any) -> Any:
    def wrapper(data: Any) -> Any:
        items = {round(x): round(x) * 2 for x in data}
        return func(items)

    return wrapper


def arrow(func: Any) -> Any:
    def wrapper(data: Any) -> Any:
        items = [f"{k} -> {v}" for k, v in data.items()]
        return func(items)

    return wrapper


@number_filter
@round_dict
@arrow
def like_numbers(data: Any) -> str:
    return (
        "I like to filter, rounding, doubling, store and decorate numbers: "
        + ", ".join(data)
        + "!"
    )
