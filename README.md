# penvm-jupyter-demos

This repository container PENVM demos running under a Jupyter environment.

JupyterLab (or the classic Jupyter), from [jupyter.org](jupyter.org), is a web-based interactive development environment supporting many programming languages, including Python, which is what PENVM uses.

Notebooks are provided to facilitate interactive demonstrations.

## Setup

### JupyterLab

See [JupyterLab install](https://jupyter.org/install) for details.

### PENVM

See [penvm](https://github.com/penvm/penvm) for details.

### Demos

```
mkdir ~/tmp/penvm-jupyter-demos
cd ~/tmp/penvm-jupyter-demos
git clone https://github.com/penvm/penvm-jupyter-demos
cd penvm-jupyter-demos
```

## Run

### Start JupyterLab

For example:
```
cd ~/tmp/penvm-jupyter-demos/penvm-jupyter-demos
~/.local/bin/jupyter-lab &
```

The demos should show up in the left sidebar.

### Run Demos

Files:

* `penvm-0.1.0-setup.ipynb` - Configures and loads basic environment. All demos depend on this notebook.
* `penvm-boot.ipynb` - Boot a basic network of machines.
* `penvm-execute.ipynb` - Run an executable.
* `penvm-file.ipynb` - File operations.
* `penvm-input-workers.ipynb` - Input worker for concurrent processing.
* `penvm-kernel.ipynb` - Kernel operations.
* `penvm-kvstore.ipynb` - Key-value store operations.
* `penvm-mandelbrot.ipynb` - Mandelbrot using workers.
    * `mandelbrotlib.py` - Library.
* `penvm-processor.ipynb` - Processor operations.
* `penvm-python.ipynb` - Run python code.
* `penvm-state.ipynb` - Collect and show state for PENVM machine objects.
* `penvm-workers.ipynb` - Workers for concurrent processing.
* `world-1-local.penvm` - 1 host (localhost) "world" file.
* `world-2-local.penvm` - 2 host (localhost) "world" file.
* `world-4-local.penvm` - 4 host (localhost) "world" file.

Start with `penvm-boot.ipynb`.

## Troubleshooting

Each PENVM carries state (settings that are affected over the course of its use) and operations must be ordered correctly to work.

Restart the Jupyter kernel when trying out the demos. This can be done using the menu option: "Kernel -> Restart Kernel ...". If all else fails, shutdown ("File -> Shutdown") and restart Jupyter.

The current release depends on PENVM being deployed as release 0.1.0.
