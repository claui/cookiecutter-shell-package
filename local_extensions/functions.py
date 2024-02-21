"""Local extension with custom functions."""

import re

from jinja2 import Environment
from jinja2.ext import Extension


class CustomFunctionsExtension(Extension):  # pylint: disable=abstract-method
    """Custom additions to Jinja’s global-function space."""

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        def _regex_replace(input_value, pattern, repl, **kwargs) -> str:
            return re.sub(pattern, repl, input_value, **kwargs)

        # Replace regular expressions via Jinja
        environment.filters["regex_replace"] = _regex_replace
        environment.globals["regex_replace"] = _regex_replace
