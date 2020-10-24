# Build information
<!-- TODO make filenames bold -->
<!-- TODO style code and variables -->

## Create a repo on GitHub

### Start from GitHub (Recommended)

1. Create a new repository
2. Add **project-name**
3. Add description
4. Add README.md
5. Add LICENSE (preferably GNUv3)
6. Add .gitignore
7. Clone to local using `git clone https://github.com/D-Bhatta/`**repo-name**`.git`

### Start from local

1. `git init` in a folder from commandline like *powershell*, *cmd*, *bash*, or *git bash*
2. Do some work
3. Create a new repository on GitHub
    1. Add project name
    2. Add description
    3. Add README.md
    4. Add LICENSE (preferably GNUv3)
    5. Add .gitignore
4. Add the remote repository using `git remote add origin https://github.com/D-Bhatta/`**repo-name**`.git`
5. Pull changes from remote using `git pull origin master`
6. See local changes with `git status`
7. Add local changes with `git add *` or `git add` **filename(s)** or `git commit -a -m "`**message**`"`
8. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
9. Push changes to remote with `git push --set-upstream origin master`, this also sets origin master as the remote upstream branch

## Setup Project

1. Create a VS Code workspace as **repo-name**`.code-workspace`
2. Pull changes from remote using `git pull`
3. Create a new branch using `git checkout -b` **setup**
4. `python -m venv` **environment-name**
5. Add environment file name to **.gitignore** file
6. Pull changes from remote using `git pull`
7. See local changes with `git status`
8. Add local changes with `git add *` or `git add` **filename(s)**
9. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
10. Push changes to remote with `git push origin` **branch-name**
11. Create pull request on github
12. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *grip*, and *pre-commit* to it—using the template at the end of this file
13. Check outdated system packages with `pip list --outdated`
14. Update outdated system packages with `pip install --upgrade` **package-names**
15. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
16. Install requirements using `pip install -r requirements_dev.txt`
17. Create *notebooks* folder
18. Create *tests* folder
    1. Create a *test_**project-name**.py* file using the template at the end of this file
    2. Make sure tests fail first, in keeping with good practices
19. Run tests using `pytest`
20. Fix any errors and run tests again
21. Run black to fix any style errors using `black .`
22. Create a **.travis.yml** file using the template at the end of this file
23. Create a **.pre-commit-config.yaml** file using the template at the end of this file
24. Create a **config.json** file using the template at the end of this file
25. Create a **docstrings.md** file using the template at the end of this file
26. Create a **.prettierignore** file using the template at the end of this file
27. Toggle repo on in [travis-ci](https://travis-ci.org/)
28. Install git pre-commit hooks using `pre-commit install`
29. Run pre-commit hooks once using `pre-commit run --all-files`
30. If there are pre-commit errors, fix, add changes, and recommit
31. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. See local changes with `git status`
    3. Add local changes with `git add *` or `git add` **filename(s)**
    4. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    5. If there are pre-commit errors, fix, add changes, and recommit
    6. Push changes to remote with `git push origin` **branch-name**
32. Modify *README.md* using template at the end of this file, and customise it as required.
33. Create a new Google Colab notebook as **project-name.ipynb**
34. Save it in Google Drive <!--This is primarily to take advantage of Drive's autosave feature-->
35. Export notebook to notebooks folder
36. Setup notebook
    1. Install keras, and tensorflow for CPU and GPU with

        ```python
        !pip install tensorflow
        !pip install tensorflow-gpu
        !pip install keras
        ```

    2. Import modules

        ```python
        import tensorflow as tf
        import matplotlib.pyplot as plt
        import keras
        import numpy as np
        import pandas as pd
        from google.colab import files
        ```

    3. Check version using

        ```python
        print(tf.__version__)
        print(keras.__version__)
        ```

    4. Import and unzip datasets using

        ```python
        !wget -cq **dataset-file-link**
        ```

        ```python
        !wget -cq **zip-file-link**
        !unzip -qq **zip-file**
        ```

    5. Add check for GPU usage using

        ```python
        device_name = tf.test.gpu_device_name()
        if device_name != '/device:GPU:0':
            raise SystemError("GPU device not found")
        print(f'Found GPU at: {device_name}')
        ```

37. Export notebook to notebooks folder
38. Merge PR
39. Checkout master branch with `git checkout master`
40. Pull changes from remote using `git pull`
41. Create a new branch using `git checkout -b` **branch-name**
42. Do your work
43. Export **project-name.py** file
44. Update *README.md*
45. Print *README.md* with `grip --export README.md`

## Templates

### requirements_dev.txt

```text
black==19.10b0
grip==4.5.2
pip==20.2
pre-commit==2.6.0
pytest==6.0.1
pytest-cov==2.10.0
wheel==0.34.2
```

### test_**project-name**.py

```python
""" Tests for 'project-name'"""
import pytest
def test_basic():
    assert 2 == 3 , "This is supposed to fail"
```

### .travis.yml

```yaml
---

dist: xenial
language: python
python: 3.8.3
install:
  - pip install -r requirements_dev.txt
script:
  - black --line-length=79 --check .
env:
  - PYTHONBREAKPOINT=0

```

### .pre-commit-config.yaml

```yaml
---
repos:
  - repo: "https://github.com/psf/black"
    rev: 19.10b0
    hooks:
      - id: black
        args: [--line-length=79]
  - repo: "https://github.com/pre-commit/pre-commit-hooks"
    rev: v3.2.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: debug-statements
      - id: check-merge-conflict
      - id: check-xml
      - id: check-json
      - id: check-docstring-first
      - id: requirements-txt-fixer
      - id: detect-private-key
  - repo: "https://github.com/asottile/blacken-docs"
    rev: v1.7.0
    hooks:
      - id: blacken-docs
        additional_dependencies:
          - black==19.3b0
  - repo: "https://github.com/asottile/setup-cfg-fmt"
    rev: v1.11.0
    hooks:
      - id: setup-cfg-fmt
  - repo: "https://github.com/timothycrosley/isort"
    rev: 5.2.2
    hooks:
      - id: isort
  - repo: "https://github.com/pre-commit/pygrep-hooks"
    rev: v1.5.1
    hooks:
      - id: rst-backticks
  - repo: "https://github.com/adrienverge/yamllint.git"
    rev: v1.24.2
    hooks:
      - id: yamllint
        args:
          - "--format"
          - parsable
          - "--strict"
  - repo: "https://github.com/Lucas-C/pre-commit-hooks-lxml"
    rev: v1.1.0
    hooks:
      - id: forbid-html-img-without-alt-text
  - repo: "https://github.com/Lucas-C/pre-commit-hooks-markup"
    rev: v1.0.0
    hooks:
      - id: rst-linter
  - repo: https://github.com/prettier/prettier
    rev: "2.1.2"
    hooks:
      - id: prettier
```

### README.md

~~~markdown
# Heading

Subheading

## Sections

1. Load Data
2. .

## Notes

1. .

```python

```

## Output

```markdown

```

## Figures

Add figures

## Project status

Project is
~~~

### Config.json

```json
{
  "logging": {
    "version": 1,
    "formatters": {
      "simple": {
        "format": "%(name)s - %(asctime)s-%(process)d-%(levelname)s-%(message)s"
      }
    },
    "handlers": {
      "console": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "simple",
        "stream": "ext://sys.stdout"
      },
      "fileHandler": {
        "class": "logging.FileHandler",
        "level": "DEBUG",
        "formatter": "simple",
        "filename": "server.log",
        "mode": "w"
      }
    },
    "loggers": {
      "appLogger": {
        "level": "DEBUG",
        "handlers": ["console", "fileHandler"],
        "propagate": false
      }
    },
    "root": {
      "level": "DEBUG",
      "handlers": ["console"]
    }
  }
}

```

### docstrings.md

~~~markdown
# Docstrings

## Sections

- [Docstrings](#docstrings)
  - [Sections](#sections)
  - [Method docstring](#method-docstring)
  - [Class docstring](#class-docstring)
  - [Module docstring](#module-docstring)

## Method docstring

```python
r"""Summarize the function in one line.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    *args : iterable
        Other arguments.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    **kwargs : dict
        Keyword arguments.

    Returns
    -------
    type
        Explanation of anonymous return value of type ``type``.
    describe : type
        Explanation of return value named `describe`.
    out : type
        Explanation of `out`.
    type_without_description

    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation.
    common_parameters_listed_above : type
        Explanation.

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    numpy.array : Relationship (optional).
    numpy.ndarray : Relationship (optional), which could be fairly long, in
                    which case the line wraps here.
    numpy.dot, numpy.linalg.norm, numpy.eye

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a Greek symbol like :math:`\omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\nb")
    a
    b
    """
```

Source: https://gist.github.com/jakevdp/3808292

## Class docstring

```python
r"""The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Parameters
    ----------
    attr1 : str
        Description of `attr1`.
    attr2 : :obj:`int`, optional
        Description of `attr2`.

    Methods
    ----------
    method_name(c='rgb')
        Description of public `method_name`.
    method_name(signature)
        Description of public `method_name`.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> from view_api.models import APIInfo
    >>> a1 = APIInfo(
    ...     name = "APOD",
    ...     description = "Astronomy Picture of the Day",
    ...     link = "https://api.nasa.gov/planetary/apod",
    ...     image = "img/1.jpg",
    ... )
    >>> a1.save()
    asyncio - 2020-10-18 05:53:05,483-5384-DEBUG-Using proactor: IocpProactor
    >>> a2 = APIInfo(
    ...     name = "EPIC",
    ...     description = "Latest Images from Earth Polychromatic Imaging Camera",
    ...     link = "https://api.nasa.gov/EPIC/api/natural",
    ...     image = "img/2.png",
    ... )
    >>> ...
    >>> a2.save()
    """
```

Source: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

## Module docstring

```python
r"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
```

~~~

### .prettierignore

```config
# Ignore all YAML files:
*.yml

# Ignore all Markdown files:
*.md

```
