# {{ cookiecutter.project_title }}

## Installation

### Installing manually

Clone this repository to any directory you like.

### Installing from the AUR

Direct your favorite
[AUR helper](https://wiki.archlinux.org/title/AUR_helpers) to the
`{{ cookiecutter.package_name }}` package.

## Usage

(tbd)

## Contributing to {{ cookiecutter.project_title }}

See [`CONTRIBUTING.md`](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}/blob/main/CONTRIBUTING.md).

## License

{% if cookiecutter.project_license == "Apache-2.0" -%}
{% include 'licenses/Apache-2.0-reference.md' %}
{%- elif cookiecutter.project_license == "Proprietary" -%}
{% include 'licenses/Proprietary-reference.md' %}
{%- endif -%}
