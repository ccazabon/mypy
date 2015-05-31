# Stubs for gettext (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class NullTranslations:
    def __init__(self, fp=None): pass
    def add_fallback(self, fallback): pass
    def gettext(self, message): pass
    def lgettext(self, message): pass
    def ngettext(self, msgid1, msgid2, n): pass
    def lngettext(self, msgid1, msgid2, n): pass
    def info(self): pass
    def charset(self): pass
    def output_charset(self): pass
    def set_output_charset(self, charset): pass
    def install(self, names=None): pass

class GNUTranslations(NullTranslations):
    LE_MAGIC = ...  # type: Any
    BE_MAGIC = ...  # type: Any
    def lgettext(self, message): pass
    def lngettext(self, msgid1, msgid2, n): pass
    def gettext(self, message): pass
    def ngettext(self, msgid1, msgid2, n): pass

def find(domain, localedir=None, languages=None, all=False): pass
def translation(domain, localedir=None, languages=None, class_=None, fallback=False,
                codeset=None): pass
def install(domain, localedir=None, codeset=None, names=None): pass
def textdomain(domain=None): pass
def bindtextdomain(domain, localedir=None): pass
def dgettext(domain, message): pass
def dngettext(domain, msgid1, msgid2, n): pass
def gettext(message): pass
def ngettext(msgid1, msgid2, n): pass

Catalog = ...  # type: Any
