from utils import TemplateEngine
from utils import HTML
from utils import Color
from utils import Slider
from utils import url

from renderers import plugin
from renderers import autocomplete
from renderers import colorpicker
from renderers import date
from renderers import datetime
from renderers import slider
from renderers import selectable
from renderers import selectables
from renderers import radioset
from renderers import checkboxset
from renderers import tinymce
from renderers import markdown
from renderers import textile
from renderers import bbcode
from renderers import default_renderers

from forms import Tabs
from forms import Accordion
from forms import MultiFieldSet

try:
    from fa.jquery.pylons import relation
    from fa.jquery.pylons import relations
except ImportError:
    pass

try:
    from fa.jquery.pyramid.renderers import relation
    from fa.jquery.pyramid.renderers import relations
except ImportError:
    pass

def includeme(config):
    config.add_translation_dirs('fa.jquery:locale/')
    config.override_asset(
        to_override="pyramid_formalchemy:templates/admin/",
        override_with="fa.jquery:templates/admin/")
    config.override_asset(
        to_override="pyramid_formalchemy:templates/forms/",
        override_with="fa.jquery:templates/forms/")

    config.add_route('markup_parser', '/markup_parser.html')
    config.add_view('fa.jquery.pyramid.markup_parser',
                    route_name='markup_parser')

    config.scan("fa.jquery.pyramid")
