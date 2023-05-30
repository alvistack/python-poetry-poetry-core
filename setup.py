# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry',
 'poetry.core',
 'poetry.core._vendor.fastjsonschema',
 'poetry.core._vendor.lark',
 'poetry.core._vendor.lark.__pyinstaller',
 'poetry.core._vendor.lark.grammars',
 'poetry.core._vendor.lark.parsers',
 'poetry.core._vendor.lark.tools',
 'poetry.core._vendor.packaging',
 'poetry.core._vendor.tomli',
 'poetry.core.constraints',
 'poetry.core.constraints.generic',
 'poetry.core.constraints.version',
 'poetry.core.exceptions',
 'poetry.core.json',
 'poetry.core.masonry',
 'poetry.core.masonry.builders',
 'poetry.core.masonry.utils',
 'poetry.core.packages',
 'poetry.core.packages.utils',
 'poetry.core.pyproject',
 'poetry.core.spdx',
 'poetry.core.utils',
 'poetry.core.vcs',
 'poetry.core.version',
 'poetry.core.version.grammars',
 'poetry.core.version.pep440']

package_data = \
{'': ['*'],
 'poetry.core': ['_vendor/*'],
 'poetry.core.json': ['schemas/*'],
 'poetry.core.spdx': ['data/*']}

setup_kwargs = {
    'name': 'poetry-core',
    'version': '1.8.1',
    'description': 'Poetry PEP 517 Build Backend',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/python-poetry/poetry-core',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
