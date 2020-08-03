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
10. Push changes to remote with `git push origin setup`
11. Create pull request on github
12. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *twine*, *grip*, *pre-commit*, and *coveralls* to it—using the template at the end of this file
13. Check outdated system packages with `pip list --outdated`
14. Update outdated system packages with `pip install --upgrade` **package-names**
15. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
16. Install requirements using `python -m pip install -r requirements_dev.txt`
17. Create primary project folder  as **project-name** and inside it
    1. Create primary python file with same name as **project-name.py**
    2. Add a hello world function, with one arg, that the function then prints to **project-name.py**—just like template at the end of this file
    3. Create **__init__.py** and leave it empty
18. Create **setup.py** file using template at the end of this file
19. Build project using `python setup.py sdist bdist_wheel`
20. Install in **environment-name** using `pip install -e .`
21. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Write tests first capturing output, and then checking *TypeError*, as in template functions at the end of this file
    3. Make sure tests fail first, in keeping with good practices
22. Run tests using `pytest`
23. Run test coverage using `pytest --cov=`**project-name**
24. Fix any errors and run tests again
25. Run black to fix any style errors using `black .`
26. If there are any build artefacts delete them
27. Update build version in **setup.py**
28. Build project using `python setup.py sdist bdist_wheel`
29. Create **.pypirc** file in home directory (User folder of PC) using the template at the end of this file
30. Publish to TestPyPl with `twine upload -r testpypi dist/**`
31. Create a test environment using `python -m venv` **environment-name-test**
32. Add environment file name to **.gitignore** file
33. Activate environment by executing it's **environment-name-test**`\Scripts\`**activate.bat** file in *cmd*
34. Install package into environment using `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple` **project-name**
35. Test whether package works by calling *helloworld* function in IPython
36. Fix any errors and run tests again
37. Run black to fix any style errors using `black .`
38. Update build version in **setup.py**
39. Build project using `python setup.py sdist bdist_wheel`
40. Publish to TestPyPl with `twine upload -r testpypi dist/**`
41. Create a **.travis.yml** file using the template at the end of this file
42. Create a **.pre-commit-config.yaml** file using the template at the end of this file
43. Toggle repo on in [travis-ci](https://travis-ci.org/)
44. Toggle repo on in [coveralls](https://coveralls.io/)
45. Install git pre-commit hooks using `pre-commit install`
46. Run pre-commit hooks once using `pre-commit run --all-files`
47. If there are pre-commit errors, fix, add changes, and recommit
48. Push changes to remote with `git push origin setup`
49. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. Fix any [coveralls](https://coveralls.io/) errors
    3. See local changes with `git status`
    4. Add local changes with `git add *` or `git add` **filename(s)**
    5. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    6. If there are pre-commit errors, fix, add changes, and recommit
    7. Push changes to remote with `git push origin` **branch-name**
50. Merge PR
51. Toggel repo on [PyUp](https://pyup.io/)

## Templates

### requirements_dev.txt

```txt
black==19.10b0
coveralls==2.1.1
grip==4.5.2
pip==20.2
pre-commit==2.6.0
pytest==6.0.1
pytest-cov==2.10.0
twine== 3.2.0
wheel==0.34.2
```

### project-name.py

```python
def helloworld(object):
    """ 
    Print a line 
    args:
        object (str): name of the object
    returns:
        None
    """
    if type(object) != str:
        raise TypeError

    print("I am a {}.".format(object))
```

### setup.py

```python
from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="project-name",
    version="0.0.1",
    author="D-Bhatta",
    author_email="email",
    description="project-description",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/**repo-name**.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: python-version",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
```

### test_project-name.py

```python
""" Tests for 'project-name' package """
import pytest
from project-name import project-name

def test_helloworld(capsys):
    """ Correct object argument prints """
    project-name.helloworld("cat")
    captured = capsys.readouterr()
    assert "cat" in captured.out
def test_helloworld_exception():
    with pytest.raises(TypeError):
        project-name.helloworld(1)
```

### .pypirc file

    [disutils]
    index-servers = 
        testpypi
    [testpypi]
    repository: https://test.pypi.org/legacy/
    username = D-Bhatta
    password = password-for-user

### .travis.yml

```yaml
---

dist: xenial
language: python
python: 3.8.3
install:
  - pip install -r requirements_dev.txt
  - pip install -e .
script:
  - black --check .
  - pytest
  - pytest --cov=project-name --cov-fail-under=100
after_success:
  - coveralls
env:
  - PYTHONBREAKPOINT=0
```

### .pre-commit-config.yaml

```yaml
---

repos:
  - repo: 'https://github.com/psf/black'
    rev: 19.10b0
    hooks:
      - id: black
  - repo: 'https://github.com/pre-commit/pre-commit-hooks'
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
  - repo: 'https://github.com/asottile/blacken-docs'
    rev: v1.7.0
    hooks:
      - id: blacken-docs
    additional_dependencies:
      - black==19.3b0
  - repo: 'https://github.com/asottile/setup-cfg-fmt'
    rev: v1.11.0
    hooks:
      - id: setup-cfg-fmt
  - repo: 'https://github.com/timothycrosley/isort'
    rev: 5.2.2
    hooks:
      - id: isort
  - repo: 'https://github.com/pre-commit/pygrep-hooks'
    rev: v1.5.1
    hooks:
      - id: rst-backticks
  - repo: 'https://github.com/adrienverge/yamllint.git'
    rev: v1.24.2
    hooks:
      - id: yamllint
    args:
      - '--format'
      - parsable
      - '--strict'
  - repo: 'https://github.com/Lucas-C/pre-commit-hooks-lxml'
    rev: v1.1.0
    hooks:
      - id: forbid-html-img-without-alt-text
  - repo: 'https://github.com/Lucas-C/pre-commit-hooks-markup'
    rev: v1.0.0
    hooks:
      - id: rst-linter

```
