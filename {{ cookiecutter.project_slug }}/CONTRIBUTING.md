# Contributing to {{ cookiecutter.project_title }}

## Setting up {{ cookiecutter.project_title }} for development

To set up {{ cookiecutter.project_title }} for development, you need
Bash and Shellcheck installed on your system.

## Generating the man page

To generate the man page, run:

```shell
sphinx-build -aqEW -b man doc/sphinx build/man
```

Note: This requires the `myst-parser` and `sphinx` Python packages
to be installed.

To open the generated man page, run:

```shell
man build/man/{{ cookiecutter.first_executable_name }}.1
```

## Running the linter

To execute the linter, run:

```shell
shellcheck bin/* libexec/*.bash
```
