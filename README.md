# nbtag

Set cell tags in a Jupyter notebook from a special comment.

## Why use this extension?

Many tools in the Jupyter ecosystem (ex.
[nbmake](https://github.com/treebeardtech/nbmake),
[nbstripout](https://github.com/kynan/nbstripout)) use cell tags to configure
their behavior.

However, some frontends to Jupyter (ex.
[ein](https://github.com/millejoh/emacs-ipython-notebook)) can't modify tags.

This server extension watches for a special comment in the content of the cell
and sets tags correspondingly.

## How to use

```python
# %tags: keep_output, another_tag
print("Hello World!")
```

A cell containing the text above will be given the tags `keep_output`,
`another_tag` on saving.

## Install

`pip install nbtag`

If you use `pipx`, make sure to inject `nbtag` into the Jupyter package's
environment.

## Enable

`jupyter serverextension enable nbtag`

`jupyter serverextension list`

## Compatibility

Only works with `jupyter server`, not with `jupyter notebook`, but I think you
should be using `jupyter server` + `nbclassic` instead of `jupyter notebook`
anyway?
