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
9. Create *notebooks* folder
10. Pull changes from remote using `git pull`
11. See local changes with `git status`
12. Add local changes with `git add *` or `git add` **filename(s)**
13. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
14. Push changes to remote with `git push`
15. Create a new branch using `git checkout -b` **branch-name**
16. Create *tests* folder
    1. Create a *test_**project-name**.py* file
    2. Make sure tests fail first, in keeping with good practices
17. Run tests using `pytest`
18. Fix any errors and run tests again
19. Run black to fix any style errors using `black` **project-name**`/` and `black tests/`
20. Pull changes from remote using `git pull`
21. See local changes with `git status`
22. Add local changes with `git add *` or `git add` **filename(s)**
23. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
24. Push changes to remote with `git push origin` **branch-name**
25. Create pull request on github
26. Merge PR
27. Create a new branch using `git checkout -b` **branch-name**
28. Create a **.travis.yml** file using the template at the end of this file
29. Create a **.pre-commit-config.yaml** file using the template at the end of this file
30. Toggle repo on in [travis-ci](https://travis-ci.org/)
31. Install git pre-commit hooks using `pre-commit install`
32. Run pre-commit hooks once using `pre-commit run --all-files`
33. Pull changes from remote using `git pull`
34. See local changes with `git status`
35. Add local changes with `git add *` or `git add` **filename(s)**
36. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
37. If there are pre-commit errors, fix, add changes, and recommit
38. Push changes to remote with `git push origin` **branch-name**
39. Create pull request on github
40. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. See local changes with `git status`
    3. Add local changes with `git add *` or `git add` **filename(s)**
    4. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    5. Push changes to remote with `git push origin` **branch-name**
41. Merge PR
42. Create a new branch using `git checkout -b` **branch-name**
43. Modify *README.md* using template at the end of this file, and customise it as required.
44. Pull changes from remote using `git pull`
45. See local changes with `git status`
46. Add local changes with `git add *` or `git add` **filename(s)**
47. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
48. If there are pre-commit errors, fix, add changes, and recommit
49. Push changes to remote with `git push origin` **branch-name**
50. Create pull request on github
51. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. See local changes with `git status`
    3. Add local changes with `git add *` or `git add` **filename(s)**
    4. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    5. Push changes to remote with `git push origin` **branch-name**
52. Merge PR
53. Create a new branch using `git checkout -b` **branch-name**
54. Create a new Google Colab notebook as **project-name.ipynb**
55. Save it in Google Drive <!--This is primarily to take advantage of Drive's autosave feature-->
56. Export notebook to notebooks folder
57. Setup notebook
    1. Install keras, and tensorflow for CPU and GPU with

        ```python
        !pip install tensorflow
        !pip install tensorflow-gpu
        !pip install keras
        ```

    2. Check version using

        ```python
        print(tf.__version__)
        print(keras.__version__)
        ```

    3. Import and unzip datasets using

        ```python
        !wget -cq **dataset-file-link**
        ```

        ```python
        !wget -cq **zip-file-link**
        !unzip -qq **zip-file**
        ```

    4. Add check for GPU usage using

        ```python
        device_name = tf.test.gpu_device_name()
        if device_name != '/device:GPU:0':
            raise SystemError("GPU device not found")
        print(f'Found GPU at: {device_name}')
        ```

58. Export notebook to notebooks folder
59. Pull changes from remote using `git pull`
60. See local changes with `git status`
61. Add local changes with `git add *` or `git add` **filename(s)**
62. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
63. If there are pre-commit errors, fix, add changes, and recommit
64. Push changes to remote with `git push origin` **branch-name**
65. Create pull request on github
66. If build fails
    1. Fix any [travis-ci](https://travis-ci.org/) errors
    2. See local changes with `git status`
    3. Add local changes with `git add *` or `git add` **filename(s)**
    4. Commit local changes with `git commit` *return, followed by typing a commit message out with a title and a body in an editor* or `git commit -m "`**message**`"`
    5. Push changes to remote with `git push origin` **branch-name**
67. Merge PR
68. Export **project-name.py** file
69. Update *README.md*
70. Print *README.md* with `grip --export README.md`

## Templates

### requirements_dev.txt

    black==19.10b0
    grip==4.5.2
    pip==20.1.1
    pre-commit==2.5.1
    pytest==5.4.3
    pytest-cov==2.9.0
    wheel==0.34.2

### Test functions Template

    """ Tests for 'project-name'"""
    import pytest
    def test_basic():
        assert 2 == 3 , "This is supposed to fail"

### .travis.yml Template

    dist: xenial
    language: python
    python: 3.8.3
    install:
    - pip install -r requirements_dev.txt
    script:
    - black --check
    - pytest
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
      - repo: 'https://github.com/Lucas-C/pre-commit-hooks-markup'
        rev: v1.0.0
        hooks:
          - id: rst-linter

### README.md

    # Heading

    Subheading

    ## Sections

    1. Load Data
    2. 

    ## Notes

    1. 

    ```python
    
    ```

    ## Output

    ```markdown
    
    ```

    ## Figures

    Add figures

    ## Project status

    Project 
