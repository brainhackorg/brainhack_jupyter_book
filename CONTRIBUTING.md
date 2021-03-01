# CONTRIBUTING

## Open Issue on GitHub

If you would like to contribute, make bug report/fix, participate in language
translation work or if you have any other queries please do not hesitate to open
an issue using one of the
[issue templates](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose)

## Making a PR

If you want to contribute with your ideas and suggestions please make a
[pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
by following the
[Template format](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose)
to the repository of the
[book](https://github.com/brainhackorg/brainhack_jupyter_book). The more
suggestions and ideas are shared and contributed by the members of the
community, this book will be a more beneficial source for the community.

## What, Where

- All the text for each chapter of the `book` lives inside the folder
  `./Brainhack Book` directory.

- All figures associated with the chapters are stored in and linked from the
  `./Brainhack Book/figures` directory.

- Everything else is in the `Brainhack Book/` directory.

### Configuration

- The table of contents (TOC) defines the order of chapters as they appear in
  the book. To change the TOC, please edit `./brainhack_book/_toc.yml` with
  correct information of filenames and their relative locations in this
  repository. Documentation on controlling the TOC structure can be found on the
  [jupyter book website](https://jupyterbook.org/customize/toc.html).

- Same applies for more general configuration using
  `./brainhack_book/_config.yml`. Documentation on configuring book settings can
  be found on the
  [jupyter book website](https://jupyterbook.org/customize/config.html).

## Deploying

The site is built and deployed automatically using a
[Github action](.github/workflows/book.yml), from the `main` branch.

## Viewing the Brainhack Book

You will need a recent version of Python to work on the book and view it
locally. If you do not have Python on your computer, we warmly recommend the
install instruction from the
[datalad handbook](http://handbook.datalad.org/en/latest/intro/installation.html#python-3-all-operating-systems).

If you are using an earlier version of Windows than Windows 10, you might want
to check the install instruction for Python and bash from
[this page from the neurohackademy](https://neurohackademy.org/setup/).

Note the install procedure below requires you to have
[git](https://git-scm.com/downloads) installed on your computer.

### Clone the project:

```bash
git clone git@github.com:brainhackorg/brainhack_jupyter_book.git
cd brainhack_book
```

### Installing Dependencies in a virtual environment

[Virtual environments](https://the-turing-way.netlify.app/reproducible-research/renv/renv-options.html)
are a great way of isolating project-related dependencies from your system-level
Python installation.

For more details on virtual environments using a tool like `venv` in Python see
[here](https://docs.python.org/3/tutorial/venv.html).

You can also use Conda that acts both as a way to manage your environments and
install packages. For more info about Conda, you can check this page of the
[Turing Way project](https://the-turing-way.netlify.app/reproducible-research/renv/renv-package.html).

To use a virtual environment for building the book project, run the following
from within the root folder of the brainhack jupyter book directory:

1. If you are using `virtualenv`:

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

2. If you are using conda:

```bash
conda env update -n brainhack-jb-env -f ./environment.yml
```

### Building the book locally

Finally, to build the book and preview your changes locally you can run the
following command:

```bash
jupyter-book build brainhack_book
```

Now you can open the HTML path provided by jupyter-book as output in your
terminal i.e. `brainhack_book/_build/html/index.html`.

### Clean up the recent build

When you test your edits by building the book multiple times, it is better to
clean up the last build before generating a new one. You can either manually
delete the `brainhack_book/_build` folder every time, or run this command:

```bash
jupyter-book clean brainhack_book
```

More details on this process can be read on the
[JupyterBook's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#clean-your-books-generated-files).

### Check external links in the book

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

<!--#### On Netlify

Brainhack book is built and deployed online using [Netlify](https://www.netlify.com/).

//If you want to deploy the book on Netlify, you'll need the following settings:

//- Base directory: `book/website`
//- Build command: `pip install -r requirements.txt && jupyter-book build .`
//- Publish directory: `book/website/_build/html`

//Netlify is smart and will find your requirements.txt to do the install for //you. :slightly_smiling_face:

You can find the build history or logs for Brainhack at https://app.netlify.com/sites/brainhack/deploys.-->

## Bibliography

In the directory `./Brainhack Book/_bibliography` a collection of bibliography
from all the chapters exist in the `references.bib` file. More details can be
read on th
[CONTRIBUTING.md](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/contributing_guideline.md)
file.

<!-- I will create one once we decide on the contribution method and workflow -->

## How to Interact With This Book

Below the interactive features of this Jupyter Book are explained in further
detail.

## Open Jupyter Notebook in the Cloud

You can open most pages from this book in the cloud and run the code live. Hover
over the rocket icon at the top of the page and click "Binder" to open a version
of the same page in the cloud.

[Binder](https://mybinder.org/) is a service that allows you to run Jupyter
notebooks without any prior configuration or installation. It may take a few
minutes for the Jupyter notebook to load, so be patient.

## Download Jupyter Notebook

You can download any Jupyter notebook page from this book as a Jupyter notebook
file (`.ipynb`). Hover over the download icon and click `".ipynb"`

**Attention!** To work with this `.ipynb` file, you will need to have Jupyter
installed and running on your own computer.

## Download PDF

You can download any Jupyter notebook page from this book as a PDF file. Hover
over the download icon and click ".pdf"

## Make Full Screen

To make any page from this book full screen, click the full screen icon at the
top of the page.

## Click to Show the Content

You can access to he content of the book by clicking "Click to Show" beneath the
cell on the right.

## Authors

This book is built and maintained by the Brainhack community. The book is open
and freely available to the community's contributions.
