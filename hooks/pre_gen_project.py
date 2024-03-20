"""
{# See https://wiki.archlinux.org/title/PKGBUILD#license #}
{%
    set spdx_license_dict = {
        "Apache-2.0": "Apache-2.0",
        "Proprietary": "LicenseRef-custom",
    }
%}
{{
    cookiecutter.update({
        "first_main_function":
            "__" + regex_replace(cookiecutter.first_executable_name, '[^A-Za-z0-9_]+', '_'),
        "package_name":
            cookiecutter.project_slug.replace('_', '-'),
        "spdx_license":
            spdx_license_dict[cookiecutter.project_license],
    })
}}
"""

import sys

MIN_SUPPORTED_PYTHON_VERSION = (3, 7)
if sys.version_info < MIN_SUPPORTED_PYTHON_VERSION:

    _version = ".".join(map(str, MIN_SUPPORTED_PYTHON_VERSION))
    sys.exit(
        f"""
This Cookiecutter template requires Python {_version} or higher.
"""
    )
