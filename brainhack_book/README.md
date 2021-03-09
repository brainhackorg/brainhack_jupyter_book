# Brainhack Book :book: 

[Brainhack](https://brainhack.org) refers to a series of community events, that bring together scientists from all around the world with a variety of expertise and disciplines to facilitate neuroscience research for the community by creating tools, methodologies, techniques, ideas, and guidelines.

Together with this book we aim to create a freely and openly accessible source for the community, that gives a gives a general overview about the aims, tools, and the outputs of the Brainhack events, that is open to the community's contributions. This book is also created by the Brainhack community as a supplement to the [Neuron, 2020 community paper](https://psyarxiv.com/rytjq/).

### Goals of the Book :dart:
This Brainhack Book aims to;

* create an open, freely accessible central source for about the concept of the Brainhack events.
* provide a projection about the past and future of the Brainhack events.
* showcase an  overview of the scope and outputs of the events run all around the world to this day.
* curate a glossary about the Brainhack community terms.
* give interactive graphical and media content about the events.
* create a living and growing community source with the contributions from the any member of the community.


### Running the Brainhack Book :hammer_and_wrench:

This book was created with [Jupyter Book](https://jupyterbook.org/intro.html) as an open-source project for designing online interactive books.


This is the README file for Brainhack Book hosted online at dedicated [Brainhack Book](https://brainhack.org/brainhack_jupyter_book/).

For the README file of the main repository please [follow this link](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/README.md).

All the text for each chapter of the `book` lives inside the folder `./brainhack_book` directory.

All figures associated with the chapters are stored in and linked from the `./brainhack_book/figures` directory.
Everything else, including the data associated with the figures and contributors lists are in the `./brainhack_book/data` directory.

### Configuration :gear:

- The table of contents (TOC) defines the order of chapters as they appear in the book.
To change the TOC, please edit `./brainhack_book/_toc.yml` with correct information of filenames and their relative locations in this repository.
Documentation on controlling the TOC structure can be found on the [Jupyter book website](https://jupyterbook.org/customize/toc.html).
- Same applies for more general configuration using `./brainhack_book/_config.yml`.
Documentation on configuring book settings can be found on the [Jupyter book website](https://jupyterbook.org/customize/config.html).

### Deploying :rocket:

The site is built and deployed automatically using Github actions, from the `main` branch.

#### Locally (Mac / Linux Only)

Clone the project:
```
git clone git@github.com:brainhackorg/brainhack_jupyter_book.git
cd brainhack_book
```

Install the dependencies using pip; or
```
pip install -r ./requirements.txt
```

Install the dependencies using conda:
```
conda env update -n brainhack-jb-env -f ./environment.yml
```

Finally, to build the book and preview your changes locally you can run the following command:
```
jupyter-book build brainhack_book
```
Now you can open the HTML path provided by jupyter-book as output in your terminal i.e. `brainhack_book/_build/html/index.html`.

For more information regarding building at your local you can read details [here](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/brainhack_book/build_in_local_guideline.md).

#### Clean up the recent build :broom:

When you test your edits by building the book multiple times, it is better to clean up the last build before generating a new one.
You can either manually delete the `brainhack_book/_build` folder every time, or run this command:
```
jupyter-book clean brainhack_book
```
More details on this process can be read on the [JupyterBook's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#clean-your-books-generated-files).

#### Check external links in the book :white_check_mark:

When editing or reviewing this book locally, you can run the link checker with Jupyter Book to check if the external links mentioned in the book are valid.
To run the link checker, use the following command:

```
jupyter-book build brainhack_book --builder linkcheck
```

The link checker checks if each link resolves and prints the status on your terminal so that you can check and resolve any incorrect links.
Read more about this on the [JupyterBook's GitHub repository](https://github.com/executablebooks/jupyter-book/blob/master/docs/advanced/advanced.md#check-external-links-in-your-book).

#### Installing Dependencies in  a  virtual environment :arrow_up:

Virtual environments are a great way of isolating project-related dependencies from your system-level Python installation.
For more details on virtual environments in python see
[here](https://docs.python.org/3/tutorial/venv.html).
To use a virtual environment for building the book project, use

```
cd book/website
virtualenv brainhack
source brainhack/bin/activate
pip install -r requirements.txt
```

In case you want to use a specific python interpreter, specify the path as
```
virtualenv -p /usr/bin/python3.7 brainhack
```

Now you can use the `jupyter-book build .` command inside `book/website` directory as explained above.

<!--#### On Netlify

Brainhack book is built and deployed online using [Netlify](https://www.netlify.com/).

//If you want to deploy the book on Netlify, you'll need the following settings:

//- Base directory: `book/website`
//- Build command: `pip install -r requirements.txt && jupyter-book build .`
//- Publish directory: `book/website/_build/html`

//Netlify is smart and will find your requirements.txt to do the install for //you. :slightly_smiling_face:

You can find the build history or logs for Brainhack at https://app.netlify.com/sites/brainhack/deploys.-->

## Bibliography :newspaper:

In the directory `./Brainhack Book/_bibliography` a collection of bibliography from all the chapters exist in the `references.bib` file.
More details can be read on th [CONTRIBUTING.md](https://github.com/brainhackorg/brainhack_jupyter_book/blob/main/contributing_guideline.md) file. <!-- I will create one once we decide on the contribution method and workflow -->

## Content Templates :clipboard:

Templates for different types of content can be created in the `templates` directory.

As of now, the template section includes:
* `case-study-template.ipynb` a template for including interactive case studies in the book

The template can be copied to create content relevant to a chapter in the `content` directory.


## How to Interact With This Book :arrows_clockwise:

Below the interactive features of this Jupyter Book are explained in further detail. 


## Open Jupyter Notebook in the Cloud :cyclone:
You can open most pages from this book in the cloud and run the code live. Hover over the rocket icon at the top of the page and click "Binder" to open a version of the same page in the cloud.

[Binder](https://mybinder.org/) is a service that allows you to run Jupyter notebooks without any prior configuration or installation. It may take a few minutes for the Jupyter notebook to load, so be patient.



## Download Jupyter Notebook :arrow_down_small:
You can download any Jupyter notebook page from this book as a Jupyter notebook file (.ipynb). Hover over the download icon and click ".ipynb"

**Attention!** :warning:
To work with this .ipynb file, you will need to have Jupyter installed and running on your own computer.


## Download PDF :arrow_down_small:
You can download any Jupyter notebook page from this book as a PDF file. Hover over the download icon and click ".pdf"


## Make Full Screen :tv:
To make any page from this book full screen, click the full screen icon at the top of the page.



## Click to Show the Content 
You can access to he content of the book by clicking "Click to Show" beneath the cell on the right.


## Authors :memo:

This book is built and maintained by the Brainhack community. The book is open and freely available to the community's contributions.


## Open Issue on GitHub :construction:
 If you would like to contribute, make bug report/fix, participate in language translation work or if you have any other queries please do not hesitate to open an issue using one of the [issue templates](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose)

 

## Making a PR <!--I was not sure whether we will accept the contributions via PR or issues so I put the both--> :arrow_up_small:

If you want to contribute with your ideas and suggestions please make a [pull request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) by following the [Template format](https://github.com/brainhackorg/brainhack_jupyter_book/issues/new/choose) to the repository of the [book](https://github.com/brainhackorg/brainhack_jupyter_book). The more suggestions and ideas are shared and contributed by the members of the community, this book will be a more beneficial source for the community.
