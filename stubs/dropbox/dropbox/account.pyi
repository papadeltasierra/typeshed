from _typeshed import Incomplete

from stone.backends.python_rsrc import stone_base as bb

class PhotoSourceArg(bb.Union):
    other: Incomplete
    @classmethod
    def base64_data(cls, val): ...
    def is_base64_data(self): ...
    def is_other(self): ...
    def get_base64_data(self): ...

PhotoSourceArg_validator: Incomplete

class SetProfilePhotoArg(bb.Struct):
    photo: Incomplete
    def __init__(self, photo: Incomplete | None = None) -> None: ...

SetProfilePhotoArg_validator: Incomplete

class SetProfilePhotoError(bb.Union):
    file_type_error: Incomplete
    file_size_error: Incomplete
    dimension_error: Incomplete
    thumbnail_error: Incomplete
    transient_error: Incomplete
    other: Incomplete
    def is_file_type_error(self): ...
    def is_file_size_error(self): ...
    def is_dimension_error(self): ...
    def is_thumbnail_error(self): ...
    def is_transient_error(self): ...
    def is_other(self): ...

SetProfilePhotoError_validator: Incomplete

class SetProfilePhotoResult(bb.Struct):
    profile_photo_url: Incomplete
    def __init__(self, profile_photo_url: Incomplete | None = None) -> None: ...

SetProfilePhotoResult_validator: Incomplete
set_profile_photo: Incomplete
ROUTES: Incomplete
