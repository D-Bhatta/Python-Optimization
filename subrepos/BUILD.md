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
4. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *twine*, and *coveralls* to it
5. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
6. Install requirements using `pip install -r requirements_dev.txt`
7. Create primary project folder  as **project-name** and inside it
   1. Create primary python file with same name as **project-name.py**
   2. Add a hello world function, with one arg, that the function then prints to **project-name.py**—just like template at the end of this file
   3. Create **__init__.py** and leave it empty
8. Create **setup.py** file using template at the end of this file
9. Pull changes from remote using `git pull`
10. See local changes with `git status`
11. Add local changes with `git add *` or `git add` **filename(s)**
12. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
13. Push changes to remote with `git push`
14. Create a new branch using `git checkout -b` **branch-name**
15. Build project using `python setup.py sdist bdist_wheel`
16. Install in **environment-name** using `pip install -e .`
17. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Write tests first capturing output, and then checking *TypeError*, as in template functions at the end of this file
    3. Make sure tests fail first, in keeping with good practices
18. Run tests using `pytest`
19. Run test coverage using `pytest --cov=`**project-name**
20. Fix any errors and run tests again
21. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
22. If there are any build artefacts delete them
23. Update build version in **setup.py**
24. Build project using `python setup.py sdist bdist_wheel`
25. Pull changes from remote using `git pull`
26. See local changes with `git status`
27. Add local changes with `git add *` or `git add` **filename(s)**
28. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
29. Push changes to remote with `git push origin` **branch-name**
30. Create pull request on github
31. Merge PR
32. Create a new branch using `git checkout -b` **branch-name**
33. Create **.pypirc** file in home directory (User folder of PC) using the template at the end of this file
34. Publish to TestPyPl with `twine upload -r testpypi dist/**`
35. Create a test environment using `python -m venv` **environment-name-test**
36. Add environment file name to **.gitignore** file
37. Activate environment by executing it's **environment-name-test**`\Scripts\`**activate.bat** file in *cmd*
38. Install package into environment using `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple` **project-name**
39. Test whether package works by calling *helloworld* function in IPython
40. Fix any errors and run tests again
41. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
42. Update build version in **setup.py**
43. Build project using `python setup.py sdist bdist_wheel`
44. Pull changes from remote using `git pull`
45. See local changes with `git status`
46. Add local changes with `git add *` or `git add` **filename(s)**
47. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
48. Push changes to remote with `git push origin` **branch-name**
49. Create pull request on github
50. Merge PR
51. Publish to TestPyPl with `twine upload -r testpypi dist/**`
52. Create a new branch using `git checkout -b` **branch-name**
53. Create a **.travis.yml** file using the template at the end of this file
54. Toggle repo on in [travis-ci](https://travis-ci.org/)
55. Toggle repo on in [coveralls](https://coveralls.io/)
56. Pull changes from remote using `git pull`
57. See local changes with `git status`
58. Add local changes with `git add *` or `git add` **filename(s)**
59. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
60. Push changes to remote with `git push origin` **branch-name**
61. Create pull request on github
62. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. Fix any [coveralls](https://coveralls.io/) errors
    3. See local changes with `git status`
    4. Add local changes with `git add *` or `git add` **filename(s)**
    5. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    6. Push changes to remote with `git push origin` **branch-name**
63. Merge PR
64. Toggel repo on [PyUp](https://pyup.io/)

## Templates

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
