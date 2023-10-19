# LAW-XVIII-2024
The 18th Linguistic Annotation Workshop

This is the `main` branch; it contains sources for building the website.
The [website](https://sigann.github.io/LAW-XVII-2023) itself lives on the `gh-pages` branch.
To deploy changes:

    $ git checkout master
    # ...make, commit, and push changes...
    $ python3 build.py deploy
    $ git checkout gh-pages
    $ mv deploy/* .
    $ rmdir deploy
    $ git commit -a -m "deploy changes"
    $ git push


NB: Only edit the files under `pages/`, since these are the ones used by the build script. Any HTML files in the repository root will be overwritten on deployment.

NB: The two branches have been cleaned up to avoid confusion since the directory structure gets flattened during build, but used to still be present in `gh-pages`. Now the directory structure (`pages/`, `images/`, etc.) only lives on this branch (the `main` branch). The live page at `gh-pages` does not have any directories, and thus paths to, e.g., images from any html pages should not specify a directory, just the base file name.

