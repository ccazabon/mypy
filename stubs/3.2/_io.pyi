# Stubs for _io (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class _IOBase:
    def __init__(self, *args, **kwargs): pass
    @property
    def closed(self): pass
    def close(self): pass
    def fileno(self): pass
    def flush(self): pass
    def isatty(self): pass
    def readable(self): pass
    def readline(self, size: int = -1): pass
    def readlines(self, hint: int = -1): pass
    def seek(self, offset, whence=...): pass
    def seekable(self): pass
    def tell(self): pass
    def truncate(self, size: int = None) -> int: pass
    def writable(self): pass
    def writelines(self, lines): pass
    def __del__(self): pass
    def __enter__(self): pass
    def __exit__(self, exc_type, exc_val, exc_tb): pass
    def __iter__(self): pass
    def __next__(self): pass

class _BufferedIOBase(_IOBase):
    def detach(self): pass
    def read(self, size: int = -1): pass
    def read1(self, size: int = -1): pass
    def readinto(self, b): pass
    def write(self, b): pass

class _RawIOBase(_IOBase):
    def read(self, size: int = -1): pass
    def readall(self): pass

class _TextIOBase(_IOBase):
    encoding = ...  # type: Any
    errors = ...  # type: Any
    newlines = ...  # type: Any
    def detach(self): pass
    def read(self, size: int = -1): pass
    def readline(self, size: int = -1): pass
    def write(self, b): pass
