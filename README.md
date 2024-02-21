# cookiecutter-shell-package

[Cookiecutter](https://github.com/cookiecutter/cookiecutter)
template for Bash scripts with focus on packageability for various
distributions and system package managers.

## About this template

### Goals

`cookiecutter-shell-package` is an opinionated Cookiecutter template
for Bash scripts with a focus on:

- Simple package maintenance

- Organizing a shell-based application into modules

- Support for dependencies between modules

- Allowing both private and public shell functions

- [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
  (FHS) compliance

- Unified structure, i.e. you can call your scripts from your
  project directory at development time and they’re going to work
  just the same as if you call them from their installed location in
  production (`/usr/bin` or `/usr/local/bin`)

### Project structure

See
[`ARCHITECTURE.md`](https://github.com/claui/cookiecutter-shell-package/blob/main/ARCHITECTURE.md)
for details.

## Using cookiecutter-shell-package

### System requirements

To use this Cookiecutter template, you need Cookiecutter.

To install Cookiecutter, follow Cookiecutter’s [installation
instructions](https://cookiecutter.readthedocs.io/en/stable/installation.html).

### Basic usage

Once you have Cookiecutter installed, run the generator:

```shell
cookiecutter gh:claui/cookiecutter-shell-package
```

### Alternative usage

If you use `cookiecutter-shell-package` often, you can add to your
`.cookiecutterrc` an `abbreviations` section like so:

```yaml
abbreviations:
    shell: https://github.com/claui/cookiecutter-shell-package.git
```

Then, to generate a project, run:

```shell
cookiecutter shell
```

### Contributing to this Cookiecutter template

See [CONTRIBUTING.md](https://github.com/claui/cookiecutter-shell-package/blob/main/CONTRIBUTING.md).

## License

Copyright (c) 2024 Claudia Pellegrino <clau@tiqua.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).

### Additional license files

This project may include additional license files other than the
Apache License. Those are just there for the template user’s
convenience so they can choose a license for their own content.
Those licenses may not apply to this project. The only license
that applies to this project is the Apache License.
