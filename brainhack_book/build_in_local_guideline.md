# How to Build Brainhack Jupyter Book in your Local

The Brainhack book is build with [jupyter-book](https://pypi.org/project/jupyter-book/) package which helps with creating on-line book version of one of [Brainhack Book](https://github.com/brainhackorg/brainhack_jupyter_book).



If you are interested in building your own Jupyterbook from scratch you might either follow the instructions from the [Jupyter book package](https://jupyterbook.org/intro) or follow an excellent summry written by [@pabloinsente](https://github.com/pabloinsente/jupyter-book-tutorial). Here we provide a quick summary of the instructions on building the Brainhack book quickly at your local and then start contributing into this exciting project! 



## Requirements

Before start, you might need to have these listed below ready for building your book.

- [A python 3.6 or 3.7](https://www.python.org/downloads/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- If you are a Windows user for Unix commands and build functions to work properly you might either need
    -  [Linux Subsystem for Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10), 
    -  [Gitbash](https://gitforwindows.org/),
    -  [Cywin](https://www.cygwin.com/)

For other requirements please have a look at our [requirements.txt](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/requirements.txt)


## Step by Step Guideline for Building the Brainhack Book at your Local,

Now, we will create the Brainhack book using the command line, step-by-step.

### Step 1:  [Fork](https://help.github.com/articles/fork-a-repo) the [Brainhack Jupyter Book repository](https://github.com/brainhackorg/brainhack_jupyter_book) to your Github account
Click on the ‘Fork’ button near the top of the page. This creates a copy of the code under your account on GitHub. For more details on how to fork a repository see [this guide](https://help.github.com/articles/fork-a-repo/). This is now your own unique copy of the  Brainhack Jupyter Book. Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!
Make sure to [keep your fork up to date](https://help.github.com/articles/syncing-a-fork) with the master repository, otherwise, you can end up with lots of dreaded [merge conflicts](https://help.github.com/articles/syncing-a-fork).




### Step 2: [Clone](https://help.github.com/articles/cloning-a-repository) your forked  Brainhack Jupyter Book repository to your machine/computer.
While you can edit files [directly on Github](https://help.github.com/articles/editing-files-in-your-repository), sometimes the changes you want to make will be complex and you will want to use a [text editor](https://en.wikipedia.org/wiki/Text_editor) that you have installed on your local machine/computer. (One great text editor is [vscode](https://code.visualstudio.com/)).
In order to work on the code locally, you must clone your forked repository. 
To keep up with the changes in the  Brainhack Jupyter Book repository, add the [Brainhack Jupyter Book repository](https://help.github.com/articles/configuring-a-remote-for-a-fork)as a remote to your locally cloned repository.

`git remote add upstream https://github.com/brainhack_jupyter_book/…...git`

Make sure to [keep your fork up to date](https://help.github.com/articles/syncing-a-fork/) with the upstream repository.
For example, to update your master branch on your local cloned repository:

`git fetch upstream`
`git checkout master`
`git merge upstream/master`


 
### Step 3: Synchronize your master branch with the upstream master branch:

`$ git checkout master`
`$ git pull upstream master`



### Step 4: Build the book at your local

Open the terminal and navigate to the folder where you cloned the Brainhack Jupyter book by:

```bash
cd ../brainhack_jupyter_book/
```

### Step 5: Create and activate a virtual environment

It is always a good idea to create a virtual environment to isolate your dependencies for each project. This is not strictly required, yet highly recommended. Make sure you are in the `/brainhack_jupyter_book` directory in your terminal: 

```bash
cd /brainhack_jupyter_book/
```

Once there, run this in the terminal to create the virtual environment following the 3 options below based on your operating sytem or choice:

```python=

#create an virtual environment in your local copy and install related libraries with conda

conda env create -f environment.yml --prefix ./envs
conda activate ./envs
 
 
# This line creates a virtual environment called 'venv'
python3 -m venv venv 
# This line activates the virtual environment On macOS and Linux:
source venv/bin/activate 

# This line activates the virtual environment On Windows

source venv/bin/activate 
or 
.\env\Scripts\activate

# You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory. On macOS and Linux:

which python
.../env/bin/python

#On Windows:

where python
.../env/bin/python.exe

#Leaving the virtual environment. If you want to switch projects or otherwise leave your virtual environment, simply run:

deactivate

```

Once the virtual environment is activated, packages will be installed in that environment, without interfering with your python system installation.  

**HEADS UP**: if you close the terminal or deactivate `venv`, make sure to re-activate the virtual environment with `source venv/bin/activate` before typing any code.

### Step 6: install jupyter-book package

The jupyter-book package can be pip-installed like this:

```python
pip install jupyter-book
```

Now, if you run:

```bash
pip list | grep jupyter-book
```

You should see something like this (version may change) printed to the terminal:

```bash
jupyter-book       0.8
```



### Step 7: build the `html` files to deploy with `jupyter-book`

Everything is in place now. The last step before deploying the Brainhack Book site at your local is to build the `html` files like this:

```bash
jupyter-book build my-book/
```

If successful, the terminal should print something like:

```bash
================================================================================


Generated 5 new files
Skipped 0 already-built files
Your Jupyter Book is now in `_build/`.
Demo your Jupyter book with `make serve` or push to GitHub!


================================================================================
```

or you can test your site locally by navigating into your book and running 

`make serve` 

or

`make book`


### Step 9: Compile pages that need markdown tables

Some information is generated from spreadsheets in data or files downloaded from [OSF](https://osf.io/utz4d/) during the website building process. Currently they are the acknowledgements and contributors pages.

Spreadsheets for acknowledgements is stored in data but the contributor list is on OSF.

Download contributor list from [OSF](https://osf.io/utz4d/):

`make contributors`


### Step 10: Build the pages with markdown table:

`python brainhack_jupyter_book/mdtable.py` [see options in the script]

or use stuff in `Makefile`:

``` make preprint  # preprint related pages
make bookpage  # jupyter book related pages 
```

### Step 11: Cleaning your local directory
There's a make command to sweap all the files related to the local build that are not needed in the repo:

`make clean`

### Step 12: Contributing to the Brainhack Book

You may want to add some content to the Book either by modifying the files by maintaining the same structure, or adding new elements.

1. add the changes to the Brainhack book's local repo
2. rebuild the site running `jupyter-book build my-book/` again
3. push the changes to GitHub and request review from others.

Please look check the [contribution guidelines](https://docs.google.com/document/d/1IhMQSPZOBYOrJ1yd0_K0Uvd4vq0NyyZbknJav5DPArI/edit#) for more information regarding how to make contributions and PR to the repo. 