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

1. `python -m venv` **environment-name**
2. Add environment file name to **.gitignore** file
3. Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *twine*, and *coveralls* to it
4. Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
5. Install requirements using `pip install -r requirements_dev.txt`
6. Create primary project folder  as **project-name** and inside it
   1. Create primary python file with same name as **project-name.py**
   2. Add a hello world function, with one arg, that the function then prints to **project-name.py**—just like template at the end of this file
   3. Create **__init__.py** and leave it empty
7. Create **setup.py** file using template at the end of this file
8. Pull changes from remote using `git pull`
9. See local changes with `git status`
10. Add local changes with `git add *` or `git add` **filename(s)**
11. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
12. Push changes to remote with `git push`
13. Create a new branch using `git checkout -b` **branch-name**
14. Build project using `python setup.py sdist bdist_wheel`
15. Install in **environment-name** using `pip install -e .`
16. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Write tests first capturing output, and then checking *TypeError*, as in template functions at the end of this file
    3. Make sure tests fail first, in keeping with good practices
17. Run tests using `pytest`
18. Run test coverage using `pytest --cov=`**project-name**
19. Fix any errors and run tests again
20. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
21. If there are any build artefacts delete them
22. Update build version in **setup.py**
23. Build project using `python setup.py sdist bdist_wheel`
24. Pull changes from remote using `git pull`
25. See local changes with `git status`
26. Add local changes with `git add *` or `git add` **filename(s)**
27. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
28. Push changes to remote with `git push origin` **branch-name**
29. Create pull request on github
30. Merge PR
31. Create a new branch using `git checkout -b` **branch-name**
32. Create **.pypirc** file in home directory (User folder of PC) using the template at the end of this file
33. Publish to TestPyPl with `twine upload -r testpypi dist/**`
34. Create a test environment using `python -m venv` **environment-name-test**
35. Add environment file name to **.gitignore** file
36. Activate environment by executing it's **environment-name-test**`\Scripts\`**activate.bat** file in *cmd*
37. Install package into environment using `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple` **project-name**
38. Test whether package works by calling *helloworld* function in IPython
39. Fix any errors and run tests again
40. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
41. Update build version in **setup.py**
42. Build project using `python setup.py sdist bdist_wheel`
43. Pull changes from remote using `git pull`
44. See local changes with `git status`
45. Add local changes with `git add *` or `git add` **filename(s)**
46. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
47. Push changes to remote with `git push origin` **branch-name**
48. Create pull request on github
49. Merge PR
50. Publish to TestPyPl with `twine upload -r testpypi dist/**`
51. Create a new branch using `git checkout -b` **branch-name**
52. Create a **.travis.yml** file using the template at the end of this file
53. Toggle repo on in [travis-ci](https://travis-ci.org/)
54. Toggle repo on in [coveralls](https://coveralls.io/)
55. Pull changes from remote using `git pull`
56. See local changes with `git status`
57. Add local changes with `git add *` or `git add` **filename(s)**
58. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
59. Push changes to remote with `git push origin` **branch-name**
60. Create pull request on github
61. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. Fix any [coveralls](https://coveralls.io/) errors
    3. See local changes with `git status`
    4. Add local changes with `git add *` or `git add` **filename(s)**
    5. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    6. Push changes to remote with `git push origin` **branch-name**
62. Merge PR
63. Toggel repo on [PyUp](https://pyup.io/)

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
    python: 3.7.2
    install:
    - pip install -r requirements_dev.txt
    - pip install -e .
    script:
    - black hammerai/
    - pytest
    - pytest --cov=hammerai
    after_success:
    - coveralls
