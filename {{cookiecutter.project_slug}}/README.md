{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Build%20Master/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Documentation/badge.svg)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }})
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

---

## Features
* Store values and retain the prior value in memory
* ... some other functionality

## Quick Start
```python
from {{ cookiecutter.project_slug }} import Example

a = Example()
a.get_value()  # 10
```

## Installation
**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`

## Documentation
For full package documentation please visit [{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}).


## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

