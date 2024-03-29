# CONTRIBUTING

- [CONTRIBUTING](#contributing)
  - [Open Issue on GitHub :ticket:](#open-issue-on-github-ticket)
  - [Making a PR :fountain\_pen:](#making-a-pr-fountain_pen)
  - [What, Where :mag\_right:](#what-where-mag_right)
    - [Configuration :gear:](#configuration-gear)
  - [Deploying :rocket:](#deploying-rocket)
  - [Viewing the brainhack\_book :eyes:](#viewing-the-brainhack_book-eyes)
    - [Fork the Brainhack Jupyter Book repository to your Github account :trident:](#fork-the-brainhack-jupyter-book-repository-to-your-github-account-trident)
    - [Clone your forked Brainhack Jupyter Book repository to your machine/computer. :arrow\_down\_small:](#clone-your-forked-brainhack-jupyter-book-repository-to-your-machinecomputer-arrow_down_small)
    - [Synchronize your main branch with the upstream main branch: :arrows\_counterclockwise:](#synchronize-your-main-branch-with-the-upstream-main-branch-arrows_counterclockwise)
    - [Installing Dependencies in a virtual environment :arrow\_up:](#installing-dependencies-in-a-virtual-environment-arrow_up)
    - [Building the book locally :white\_check\_mark:](#building-the-book-locally-white_check_mark)
    - [Clean up the recent build :broom:](#clean-up-the-recent-build-broom)
  - [Updating the project "database" :floppy\_disk:](#updating-the-project-database-floppy_disk)
    - [Check external links in the book :link:](#check-external-links-in-the-book-link)
  - [Bibliography :newspaper:](#bibliography-newspaper)

## Open Issue on GitHub :ticket:

If you would like to contribute, make bug report/fix, participate in language
translation work or if you have any other queries please do not hesitate to open
an issue using one of the
[issue templates](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose)

## Making a PR :fountain_pen:

If you want to contribute with your ideas and suggestions please make a
[pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
by following the
[Template format](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose)
to the repository of the
[book](https://github.com/brainhackorg/brainhack_jupyter_book). The more
suggestions and ideas are shared and contributed by the members of the
community, this book will be a more beneficial source for the community.

## What, Where :mag_right:

- All the text for each chapter of the `book` lives inside the folder
  `./brainhack_book` directory.

- All figures associated with the chapters are stored in and linked from the
  `./brainhack_book/static` directory.

- Everything else is in the `brainhack_book/` directory.

### Configuration :gear:

- The table of contents (TOC) defines the order of chapters as they appear in
  the book. To change the TOC, please edit `./brainhack_book/_toc.yml` with
  correct information of filenames and their relative locations in this
  repository. Documentation on controlling the TOC structure can be found on the
  [jupyter book website](https://jupyterbook.org/customize/toc.html).

- Same applies for more general configuration using
  `./brainhack_book/_config.yml`. Documentation on configuring book settings can
  be found on the
  [jupyter book website](https://jupyterbook.org/customize/config.html).

## Deploying :rocket:

The site is built and deployed automatically using a
[Github action](.github/workflows/deploy_book.yml), from the `main` branch.

## Viewing the brainhack_book :eyes:

Before start, you might need to have these listed below ready.

- A recent version of Python ([Python](https://www.python.org/downloads/)) to
  work on the book and view it locally. If you do not have Python on your
  computer, we warmly recommend the install instruction from the
  [datalad handbook](http://handbook.datalad.org/en/latest/intro/installation.html#python-3-all-operating-systems).

If you are using an earlier version of Windows than Windows 10, you might want
to check the install instruction for Python and bash from
[this page from the neurohackademy](https://neurohackademy.org/setup/).

- Note the install procedure below requires you to have
  [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
  on your computer.

- If you are a Windows user for Unix commands and build functions to work
  properly you might either need
  - [Linux Subsystem for Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10),
  - [Gitbash](https://gitforwindows.org/),
  - [Cywin](https://www.cygwin.com/)

### [Fork](https://help.github.com/articles/fork-a-repo) the [Brainhack Jupyter Book repository](https://github.com/brainhackorg/brainhack_jupyter_book) to your Github account :trident:

Click on the ‘Fork’ button near the top of the page. This creates a copy of the
code under your account on GitHub. For more details on how to fork a repository
see [this guide](https://help.github.com/articles/fork-a-repo/).

This is now your own unique copy of the Brainhack Jupyter Book. Changes here
won't affect anyone else's work, so it's a safe space to explore edits to the
code!

Make sure to
[keep your fork up to date](https://help.github.com/articles/syncing-a-fork)
with the upstream repository, otherwise, you can end up with lots of dreaded
[merge conflicts](https://help.github.com/articles/syncing-a-fork).

### [Clone](https://help.github.com/articles/cloning-a-repository) your forked Brainhack Jupyter Book repository to your machine/computer. :arrow_down_small:

While you can edit files
[directly on Github](https://help.github.com/articles/editing-files-in-your-repository),
sometimes the changes you want to make will be complex and you will want to use
a [text editor](https://en.wikipedia.org/wiki/Text_editor) that you have
installed on your local machine/computer. (One great text editor is
[vscode](https://code.visualstudio.com/)). In order to work on the code locally,
you must clone your forked repository.

```bash
git clone git@github.com:YOURUSERNAME/brainhack_jupyter_book.git
cd brainhack_book
```

To keep up with the changes in the Brainhack Jupyter Book repository, add the
[Brainhack Jupyter Book repository](https://help.github.com/articles/configuring-a-remote-for-a-fork)
as a remote to your locally cloned repository.

The first time you try to sync your fork, you may have to set the upstream
branch:

```bash
git remote add upstream https://github.com/brainhack_jupyter_book/brainhack_jupyter_book.git
git remote -v # Making sure the upstream repo is listed.
```

Make sure to
[keep your fork up to date](https://help.github.com/articles/syncing-a-fork/)
with the upstream repository. For example, to update your main branch on your
local cloned repository:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### Synchronize your main branch with the upstream main branch: :arrows_counterclockwise:

```bash
git checkout main
git pull upstream main
```

You can then create a new branch to work on an issue. Using a new branch allows
you to follow the standard GitHub workflow when making changes. This
[guide](https://guides.github.com/introduction/flow/) provides a useful overview
of this workflow. Please keep the name of your branch short and
self-explanatory.

```bash
git checkout -b MYBRANCH
```

### Installing Dependencies in a virtual environment :arrow_up:

For the requirements please have a look at our
[requirements.txt](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/requirements.txt)

[Virtual environments](https://the-turing-way.netlify.app/reproducible-research/renv/renv-options.html)
are a great way of isolating project-related dependencies from your system-level
Python installation.

For more details on virtual environments using a tool like `venv` in Python see
[here](https://docs.python.org/3/tutorial/venv.html).

You can also use Conda that acts both as a way to manage your environments and
install packages. For more info about Conda, you can check this page of the
[The Turing Way project](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package.html).

To use a virtual environment for building the book project, run the following
from within the root folder of the brainhack jupyter book directory:

1. If you are using `venv`: either use this

```bash
# This line creates a virtual environment called 'venv'
python3 -m venv venv

# This line activates the virtual environment On macOS and Linux:
source venv/bin/activate

# This line activates the virtual environment On Windows

source venv/bin/activate
```

or you can use the following with `virtualenv`

```bash
# create a virtual environment and "activate" it
virtualenv brainhack
source brainhack/bin/activate

# install in this environment all the Python packages
# listed in the requirements.txt file
pip install -r requirements.txt
```

In case you want to use a specific python interpreter, specify the path as

```bash
virtualenv -p /usr/bin/python3.7 brainhack
```

After you create your virtual environment using either way described above, then
you can install the requirements for building the book by running

`pip install -r requirements.txt`

2. If you are using conda:

```bash
conda env update -n brainhack-jb-env -f ./environment.yml
```

In order to leaving the virtual environment. If you want to switch projects or
otherwise leave your virtual environment, simply run:

`deactivate`

Once the virtual environment is activated, packages will be installed in that
environment, without interfering with your python system installation.

**HEADS UP**: if you close the terminal or deactivate `venv`, make sure to
re-activate the virtual environment with `source venv/bin/activate` before
typing any code.

### Building the book locally :white_check_mark:

The brainhack_book is build with
[jupyter-book](https://pypi.org/project/jupyter-book/) package which helps with
creating on-line book version of one of
[brainhack_book](https://github.com/brainhackorg/brainhack_jupyter_book).

Now, if you run:

```bash
pip list | grep jupyter-book
```

You should see something like this (version may change) printed to the terminal:

```bash
jupyter-book
```

To build the book and preview your changes locally, you can run the following
command in the repository root directory:

```bash
jupyter-book build brainhack_book
```

or you can test your site locally by navigating into your book and running

```bash
make book
```

Make is a useful reproducibility tool to help you to automate the process of
building file/s from file/s they are dependent on. In order to get a better
grasp of the whole concept and learn more about its use in the reproducibility
research we recommend you to read
[The Turing Way's dedicated chapter for Make](https://the-turing-way.netlify.app/reproducible-research/make.html).

Now you can open the HTML path provided by jupyter-book as output in your
terminal i.e. `brainhack_book/_build/html/index.html`.

Note that if you want to may have to generate the figures

### Clean up the recent build :broom:

When you test your edits by building the book multiple times, it is better to
clean up the last build before generating a new one. You can either manually
delete the `brainhack_book/_build` folder every time, or run this command:

```bash
jupyter-book clean brainhack_book
```

More details on this process can be read on the
[JupyterBook's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#clean-your-books-generated-files).

## Updating the project "database" :floppy_disk:

The project "database" is set of JSON and tabular (CSV, TSV) files that contains
information about the projects.

The information about each project is stored in github issues on several
repositories.

The list of repositories is stored in the
[repositories.json](data/repositories.json) file.

The information is extracted from the issues using the github API by the script
`scripts/get_projects_issues.py` and all the projects of a given repository are
stored in a single JSON file in the data folder. To run this script you must
have a github token with the `repo` scope saved in the `scripts/token.txt` file.
DO NOT COMMIT THIS FILE.

You can get a token from your github account settings.

https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

A single table of all the projects is generated by the script
`scripts/create_projects_table.py`.

Figures are generated by the script `scripts/create_figures.py`.

### Check external links in the book :link:

When editing or reviewing this book locally, you can run the link checker with
Jupyter Book to check if the external links mentioned in the book are valid. To
run the link checker, use the following command:

```bash
jupyter-book build brainhack_book --builder linkcheck
```

The link checker checks if each link resolves and prints the status on your
terminal so that you can check and resolve any incorrect links. Read more about
this on the
[JupyterBook's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#check-external-links-in-your-book).

## Bibliography :newspaper:

In the directory `./brainhack_book/_bibliography` a collection of bibliography
from all the chapters exist in the `references.bib` file. More details can be
read on th
[CONTRIBUTING.md](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/contributing_guideline.md)
file.
