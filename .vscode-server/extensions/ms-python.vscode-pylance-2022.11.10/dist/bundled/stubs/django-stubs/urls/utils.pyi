from typing import Any, Callable, Tuple, Union

def get_callable(lookup_view: Union[Callable[..., Any], str]) -> Callable[..., Any]: ...
def get_mod_func(callback: str) -> Tuple[str, str]: ...
