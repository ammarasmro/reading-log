# Installation

```bash
pyenv virtualenv 3.8.5 reading_pelican_env
pyenv activate reading_pelican_env
```

Generate site

```bash
make html
```

Generate site with [Publish settings](./publishconf.py)

```python
make publish
```

Preview

```bash
make devserver
```

Push site to GitHub pages

```bash
make github
```

## Categories

We have several categories. Put the article in the related category folder.

## Writing an article

Make a new markdown file. Name it using kebab-case naming. The name will show at the URL, i.e., [https://ammarasmaro.com/reading-log/article-name.html](#)

Preferrably copy it from another artcile.

Change the title. No two files should contain same title.
Title could be just today's date since this is a log.

Change the date to reflect today's date. This is going to be used to determine which articles show first on the site. New comes first.

### TODO

- Edit theme
  - Perhaps add vue support
- Make date be the default title
- Add Google Tracking to see how it is doing
