
import os

# pythonz installer root path
INSTALLER_ROOT = os.path.dirname(os.path.abspath(__file__))

# Root
# pythonz root path
ROOT = os.environ.get("PYTHONZ_ROOT")
if not ROOT:
    ROOT = os.path.join(os.environ["HOME"],".pythonz")

# directories
PATH_PYTHONS = os.path.join(ROOT,"pythons")
PATH_BUILD = os.path.join(ROOT,"build")
PATH_DISTS = os.path.join(ROOT,"dists")
PATH_ETC = os.path.join(ROOT,"etc")
PATH_BIN = os.path.join(ROOT,"bin")
PATH_LOG = os.path.join(ROOT,"log")
PATH_SCRIPTS = os.path.join(ROOT,"scripts")
PATH_SCRIPTS_PYTHONZ = os.path.join(PATH_SCRIPTS,"pythonz")
PATH_SCRIPTS_PYTHONZ_COMMANDS = os.path.join(PATH_SCRIPTS_PYTHONZ,"commands")
PATH_SCRIPTS_PYTHONZ_INSTALLER = os.path.join(PATH_SCRIPTS_PYTHONZ,"installer")
PATH_PATCHES = os.path.join(ROOT,"patches")
PATH_PATCHES_ALL = os.path.join(PATH_PATCHES,"all")
PATH_PATCHES_MACOSX = os.path.join(PATH_PATCHES,"macosx")
PATH_PATCHES_MACOSX_PYTHON27 = os.path.join(PATH_PATCHES_MACOSX,"python27")
PATH_PATCHES_MACOSX_PYTHON26 = os.path.join(PATH_PATCHES_MACOSX,"python26")

# files
PATH_BIN_PYTHONZ = os.path.join(PATH_BIN,'pythonz')

# Home
# pythonz home path
PATH_HOME = os.environ.get('PYTHONZ_HOME')
if not PATH_HOME:
    PATH_HOME = os.path.join(os.environ["HOME"],".pythonz")

# directories
PATH_HOME_ETC = os.path.join(PATH_HOME, 'etc')

# pythonz download
PYTHONZ_UPDATE_URL = os.getenv('PYTHONZ_UPDATE_URL', 'https://github.com/saghul/pythonz/tarball/master')

