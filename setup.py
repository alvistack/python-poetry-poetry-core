# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry',
 'poetry.core',
 'poetry.core._vendor',
 'poetry.core._vendor.attr',
 'poetry.core._vendor.attrs',
 'poetry.core._vendor.jsonschema',
 'poetry.core._vendor.jsonschema.benchmarks',
 'poetry.core._vendor.lark',
 'poetry.core._vendor.lark.__pyinstaller',
 'poetry.core._vendor.lark.grammars',
 'poetry.core._vendor.lark.parsers',
 'poetry.core._vendor.lark.tools',
 'poetry.core._vendor.packaging',
 'poetry.core._vendor.pyrsistent',
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
 'poetry.core.packages.constraints',
 'poetry.core.packages.utils',
 'poetry.core.pyproject',
 'poetry.core.semver',
 'poetry.core.spdx',
 'poetry.core.utils',
 'poetry.core.vcs',
 'poetry.core.version',
 'poetry.core.version.grammars',
 'poetry.core.version.pep440']

package_data = \
{'': ['*'],
 'poetry.core._vendor.jsonschema': ['schemas/*',
                                    'schemas/vocabularies/draft2019-09/*',
                                    'schemas/vocabularies/draft2020-12/*'],
 'poetry.core._vendor.jsonschema.benchmarks': ['issue232/*'],
 'poetry.core.json': ['schemas/*'],
 'poetry.core.spdx': ['data/*']}

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.7.0']}

setup_kwargs = {
    'name': 'poetry-core',
    'version': '1.6.0',
    'description': 'Poetry PEP 517 Build Backend',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/python-poetry/poetry-core',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
