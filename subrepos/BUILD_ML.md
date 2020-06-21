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
2. `python -m venv` **environment-name**
3. Add environment file name to **.gitignore** file
4. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *grip*, and *pre-commit* to it—using the template at the end of this file
5. Check outdated system packages with `pip list --outdated`
6. Update outdated system packages with `pip install --upgrade` **package-names**
7. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
8. Install requirements using `pip install -r requirements_dev.txt`
9. Pull changes from remote using `git pull`
10. See local changes with `git status`
11. Add local changes with `git add *` or `git add` **filename(s)**
12. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
13. Push changes to remote with `git push`
14. Create a new branch using `git checkout -b` **branch-name**
15. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Make sure tests fail first, in keeping with good practices
16. Run tests using `pytest`
17. Fix any errors and run tests again
18. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
19. Pull changes from remote using `git pull`
20. See local changes with `git status`
21. Add local changes with `git add *` or `git add` **filename(s)**
22. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
23. Push changes to remote with `git push origin` **branch-name**
24. Create pull request on github
25. Merge PR
26. Create a new branch using `git checkout -b` **branch-name**
27. Create a **.travis.yml** file using the template at the end of this file
28. Create a **.pre-commit-config.yaml** file using the template at the end of this file
29. Toggle repo on in [travis-ci](https://travis-ci.org/)
30. Install git pre-commit hooks using `pre-commit install`
31. Run pre-commit hooks once using `pre-commit run --all-files`
32. Pull changes from remote using `git pull`
33. See local changes with `git status`
34. Add local changes with `git add *` or `git add` **filename(s)**
35. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
36. Push changes to remote with `git push origin` **branch-name**
37. Create pull request on github
38. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. Fix any [coveralls](https://coveralls.io/) errors
    3. See local changes with `git status`
    4. Add local changes with `git add *` or `git add` **filename(s)**
    5. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    6. Push changes to remote with `git push origin` **branch-name**
39. Merge PR

## Templates

### requirements_dev.txt

    black==19.10b0
    coveralls==2.0.0
    grip==4.5.2
    pip==20.1.1
    pre-commit==2.5.1
    pytest==5.4.3
    pytest-cov==2.9.0
    twine==3.1.1
    wheel==0.34.2

### Primary python file Template

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

### setup.py Template

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

### Test functions Template

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

### .pypirc file Template

    [disutils]
    index-servers = 
        testpypi
    [testpypi]
    repository: https://test.pypi.org/legacy/
    username = D-Bhatta
    password = password-for-user

### .travis.yml Template

    dist: xenial
    language: python
    python: 3.8.3
    install:
    - pip install -r requirements_dev.txt
    - pip install -e .
    script:
    - black --check project-name/
    - pytest
    - pytest --cov=project-name --cov-fail-under=100
    after_success:
    - coveralls
    env:
    - PYTHONBREAKPOINT=0

### .pre-commit-config.yaml

    repos:
      - repo: 'https://github.com/psf/black'
        rev: 19.10b0
        hooks:
          - id: black
      - repo: 'https://github.com/pre-commit/pre-commit-hooks'
        rev: v3.1.0
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
        rev: v1.9.0
        hooks:
          - id: setup-cfg-fmt
      - repo: 'https://github.com/timothycrosley/isort'
        rev: 4.3.21
        hooks:
          - id: isort
      - repo: 'https://github.com/pre-commit/pygrep-hooks'
        rev: v1.5.1
        hooks:
          - id: rst-backticks
      - repo: 'https://github.com/adrienverge/yamllint.git'
        rev: v1.23.0
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
