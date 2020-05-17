# Build information
<!-- TODO make filenames bold -->
<!-- TODO style code and variables -->
<!-- Change to numbered lists -->

## Create a repo on GitHub

### Start from GitHub (Recommended)

- Create a new repository
- Add **project-name**
- Add description
- Add README.md
- Add LICENSE (preferably GNUv3)
- Add .gitignore
- Clone to local using `git clone https://github.com/D-Bhatta/`**repo-name**`.git`

### Start from local

- `git init` in a folder from commandline like *powershell*, *cmd*, *bash*, or *git bash*
- Do some work
- Create a new repository on GitHub
  - Add project name
  - Add description
  - Add README.md
  - Add LICENSE (preferably GNUv3)
  - Add .gitignore
- Add the remote repository using `git remote add origin https://github.com/D-Bhatta/`**repo-name**`.git`
- Pull changes from remote using `git pull origin master`
- See local changes with `git status`
- Add local changes with `git add *` or `git add` **filename(s)** or `git commit -a -m "`**message**`"`
- Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
- Push changes to remote with `git push --set-upstream origin master`, this also sets origin master as the remote upstream branch

## Create an environment

- `python -m venv` **environment-name**
- Add environment file name to **.gitignore** file
- Create **requirements_dev.txt** file and add *pip*, *wheel*, *black*, *pytest*, *pytest-cov*, *twine*, and *coveralls* to it
- Activate environment by executing it's **environment-name**`\Scripts\`**activate.bat** file in *cmd*
- Install requirements using `pip install -r requirements_dev.txt`
- Create primary project folder  as **project-name** and inside it
  - Create primary python file with same name as **project-name.py**
  - Add a hello world function, with one arg, that the function then prints to **project-name.py**—just like template at the end of this file
  - Create **__init__.py** and leave it empty
- Create **setup.py** file using template at the end of this file
- Pull changes from remote using `git pull`
- See local changes with `git status`
- Add local changes with `git add *` or `git add` **filename(s)**
- Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
- Push changes to remote with `git push`
- Create a new branch using `git checkout -b` **branch-name**
- Build project using `python setup.py sdist bdist_wheel`
- Install in **environment-name** using `pip install -e .`
- Create *tests* folder
  - Create a *test_**project-name**.py* file
  - Write tests first capturing output, and then checking *TypeError*, as in template functions at the end of this file
  - Make sure tests fail first, in keeping with good practices
- Run tests using `pytest`
- Run test coverage using `pytest --cov=`**project-name**
- Fix any errors and run tests again
- Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
- If there are any build artefacts delete them
- Update build version in **setup.py**
- Build project using `python setup.py sdist bdist_wheel`
- Pull changes from remote using `git pull`
- See local changes with `git status`
- Add local changes with `git add *` or `git add` **filename(s)**
- Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
- Push changes to remote with `git push origin` **branch-name**
- Create pull request on github
- Merge PR
- Create a new branch using `git checkout -b` **branch-name**
- Create **.pypirc** file in home directory (User folder of PC) using the template at the end of this file
- Publish to TestPyPl with `twine upload -r testpypi dist/**`
- Create a test environment using `python -m venv` **environment-name-test**
- Add environment file name to **.gitignore** file
- Activate environment by executing it's **environment-name-test**`\Scripts\`**activate.bat** file in *cmd*
- Install package into environment using `pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple` **project-name**
- Test whether package works by calling *helloworld* function in IPython
- Fix any errors and run tests again
- Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
- Update build version in **setup.py**
- Build project using `python setup.py sdist bdist_wheel`
- Pull changes from remote using `git pull`
- See local changes with `git status`
- Add local changes with `git add *` or `git add` **filename(s)**
- Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
- Push changes to remote with `git push origin` **branch-name**
- Create pull request on github
- Merge PR
- Publish to TestPyPl with `twine upload -r testpypi dist/**`
- Create a new branch using `git checkout -b` **branch-name**
- Create a **.travis.yml** file using the template at the end of this file
- Toggle repo on in [travis-ci](https://travis-ci.org/)
- Toggle repo on in [coveralls](https://coveralls.io/)
- Pull changes from remote using `git pull`
- See local changes with `git status`
- Add local changes with `git add *` or `git add` **filename(s)**
- Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
- Push changes to remote with `git push origin` **branch-name**
- Create pull request on github
- If build fails
  - Fix any [travis-ci](https://travis-ci.org/) errors
  - Fix any [coveralls](https://coveralls.io/) errors
  - See local changes with `git status`
  - Add local changes with `git add *` or `git add` **filename(s)**
  - Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
  - Push changes to remote with `git push origin` **branch-name**
- Merge PR
- Toggel repo on [PyUp](https://pyup.io/)

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

### Test functions template

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
