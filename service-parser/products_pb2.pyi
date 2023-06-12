from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["articul", "description", "name", "price"]
    ARTICUL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    articul: str
    description: str
    name: str
    price: str
    def __init__(self, name: _Optional[str] = ..., articul: _Optional[str] = ..., price: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class SendProductRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SendProductResponse(_message.Message):
    __slots__ = ["products"]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    products: _containers.RepeatedCompositeFieldContainer[Product]
    def __init__(self, products: _Optional[_Iterable[_Union[Product, _Mapping]]] = ...) -> None: ...
