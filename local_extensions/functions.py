"""Local extension with custom functions."""

import re
from typing import Callable, Union, Pattern

from jinja2 import Environment
from jinja2.ext import Extension


class CustomFunctionsExtension(Extension):  # pylint: disable=abstract-method
    """Custom additions to Jinja’s global-function space."""

    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        def _regex_replace(
            input_value: str, pattern: Union[str, Pattern[str]],
            repl: Union[str, Callable[[re.Match[str]], str]],
            count: int=0, flags: Union[int, re.RegexFlag]=0,
        ) -> str:
            return re.sub(pattern, repl, input_value, count, flags)

        # Replace regular expressions via Jinja
        environment.filters["regex_replace"] = _regex_replace
        environment.globals["regex_replace"] = _regex_replace
