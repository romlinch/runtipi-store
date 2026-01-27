# Jupyter

JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning.

## Features

- **Multi-language support**: Python, R, and Julia pre-installed with the Data Science notebook image
- **Interactive notebooks**: Create and share documents containing live code, equations, visualizations, and narrative text
- **Rich output**: Display rich media outputs including HTML, LaTeX, PNG, SVG, and PDF
- **Extensions**: Extensible architecture with a growing ecosystem of extensions
- **Terminal access**: Built-in terminal for system commands
- **File browser**: Navigate and manage your files and notebooks

## Default User

The default user inside the container is `jovyan` with home directory `/home/jovyan`. Your work files are stored in `/home/jovyan/work` which is persisted on the host.

## Authentication

Set a token in the configuration to secure your Jupyter instance. If left empty, authentication is disabled (not recommended for exposed instances).

## Documentation

- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/)
