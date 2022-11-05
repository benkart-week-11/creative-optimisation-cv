from typing import Any, Callable, Iterable, Optional, Type, TypeVar, Union

from django.utils.deprecation import MiddlewareMixin
from django.views.generic.base import View

_T = TypeVar("_T", bound=Union[View, Callable[..., Any]])  # Any callable

class classonlymethod(classmethod[Any]): ...

def method_decorator(
    decorator: Union[Callable[..., Any], Iterable[Callable[..., Any]]], name: str = ...
) -> Callable[[_T], _T]: ...
def decorator_from_middleware_with_args(
    middleware_class: type,
) -> Callable[..., Callable[[_T], _T]]: ...
def decorator_from_middleware(middleware_class: type) -> Callable[[_T], _T]: ...
def available_attrs(fn: Callable[..., Any]) -> Any: ...
def make_middleware_decorator(
    middleware_class: Type[MiddlewareMixin],
) -> Callable[..., Any]: ...

class classproperty:
    fget: Optional[Callable[..., Any]] = ...
    def __init__(self, method: Optional[Callable[..., Any]] = ...) -> None: ...
    def __get__(self, instance: Any, cls: Optional[type] = ...) -> Any: ...
    def getter(self, method: Callable[..., Any]) -> classproperty: ...

def sync_and_async_middleware(func: _T) -> _T: ...
def sync_only_middleware(func: _T) -> _T: ...
def async_only_middleware(func: _T) -> _T: ...
