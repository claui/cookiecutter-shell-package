source libexec/constants.bash
source libexec/options.bash

function {{ cookiecutter.first_main_function }} {
  parse_options "$@"
  echo "${__HELLO}"
}

export -f {{ cookiecutter.first_main_function }}
