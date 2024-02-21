source libexec/constants.bash

function {{ cookiecutter.first_main_function }} {
  echo "${__HELLO}"
}

export -f {{ cookiecutter.first_main_function }}
