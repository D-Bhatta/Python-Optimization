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
4. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *twine*, *grip*, *pre-commit*, and *coveralls* to it—using the template at the end of this file
5. Check outdated system packages with `pip list --outdated`
6. Update outdated system packages with `pip install --upgrade` **package-names**
7. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
8. Install requirements using `pip install -r requirements_dev.txt`
9. Create primary project folder  as **project-name** and inside it
   1. Create primary python file with same name as **project-name.py**
   2. Add a hello world function, with one arg, that the function then prints to **project-name.py**—just like template at the end of this file
   3. Create **__init__.py** and leave it empty
10. Create **setup.py** file using template at the end of this file
11. Pull changes from remote using `git pull`
12. See local changes with `git status`
13. Add local changes with `git add *` or `git add` **filename(s)**
14. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
15. Push changes to remote with `git push`
16. Create a new branch using `git checkout -b` **branch-name**
17. Build project using `python setup.py sdist bdist_wheel`
18. Install in **environment-name** using `pip install -e .`
19. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Write tests first capturing output, and then checking *TypeError*, as in template functions at the end of this file
    3. Make sure tests fail first, in keeping with good practices
20. Run tests using `pytest`
21. Run test coverage using `pytest --cov=`**project-name**
22. Fix any errors and run tests again
23. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
24. If there are any build artefacts delete them
25. Update build version in **setup.py**
26. Build project using `python setup.py sdist bdist_wheel`
27. Pull changes from remote using `git pull`
28. See local changes with `git status`
29. Add local changes with `git add *` or `git add` **filename(s)**
30. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
31. Push changes to remote with `git push origin` **branch-name**
32. Create pull request on github
33. Merge PR
34. Create a new branch using `git checkout -b` **branch-name**
35. Create **.pypirc** file in home directory (User folder of PC) using the template at the end of this file
36. Publish to TestPyPl with `twine upload -r testpypi dist/**`
37. Create a test environment using `python -m venv` **environment-name-test**
38. Add environment file name to **.gitignore** file
39. Activate environment by executing it's **environment-name-test**`\Scripts\`**activate.bat** file in *cmd*
40. Install package into environment using `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple` **project-name**
41. Test whether package works by calling *helloworld* function in IPython
42. Fix any errors and run tests again
43. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
44. Update build version in **setup.py**
45. Build project using `python setup.py sdist bdist_wheel`
46. Pull changes from remote using `git pull`
47. See local changes with `git status`
48. Add local changes with `git add *` or `git add` **filename(s)**
49. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
50. Push changes to remote with `git push origin` **branch-name**
51. Create pull request on github
52. Merge PR
53. Publish to TestPyPl with `twine upload -r testpypi dist/**`
54. Create a new branch using `git checkout -b` **branch-name**
55. Create a **.travis.yml** file using the template at the end of this file
56. Create a **.pre-commit-config.yaml** file using the template at the end of this file
57. Toggle repo on in [travis-ci](https://travis-ci.org/)
58. Toggle repo on in [coveralls](https://coveralls.io/)
59. Install git pre-commit hooks using `pre-commit install`
60. Run pre-commit hooks once using `pre-commit run --all-files`
61. Pull changes from remote using `git pull`
62. See local changes with `git status`
63. Add local changes with `git add *` or `git add` **filename(s)**
64. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
65. Push changes to remote with `git push origin` **branch-name**
66. Create pull request on github
67. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. Fix any [coveralls](https://coveralls.io/) errors
    3. See local changes with `git status`
    4. Add local changes with `git add *` or `git add` **filename(s)**
    5. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    6. Push changes to remote with `git push origin` **branch-name**
68. Merge PR
69. Toggel repo on [PyUp](https://pyup.io/)

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
    -   repo: https://github.com/psf/black
        rev: 19.10b0
        hooks:
        -   id: black
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v3.1.0
        hooks:
        -   id: check-yaml
        -   id: end-of-file-fixer
        -   id: trailing-whitespace
        -   id: debug-statements
        -   id: check-merge-conflict
        -   id: check-xml
        -   id: check-json
        -   id: check-docstring-first
        -   id: requirements-txt-fixer
        -   id: detect-private-key
    -   repo: https://github.com/asottile/blacken-docs
        rev: v1.7.0
        hooks:
        -   id: blacken-docs
        additional_dependencies:
        - black==19.3b0
    -   repo: https://github.com/asottile/setup-cfg-fmt
        rev: v1.9.0
        hooks:
        -   id: setup-cfg-fmt
    -   repo: https://github.com/timothycrosley/isort
        rev: 4.3.21
        hooks:
        -   id: isort
    -   repo: https://github.com/pre-commit/pygrep-hooks
        rev: v1.5.1
        hooks:
        -   id: rst-backticks
    -   repo: https://github.com/adrienverge/yamllint.git
        rev: v1.23.0
        hooks:
        -   id: yamllint
        args:
        - --format
        - parsable
        - --strict
    -   repo: https://github.com/Lucas-C/pre-commit-hooks-lxml
        rev: v1.1.0
        hooks:
        -   id: forbid-html-img-without-alt-text
    - repo: https://github.com/Lucas-C/pre-commit-hooks-markup
      rev: v1.0.0
      hooks:
      - id: rst-linter
