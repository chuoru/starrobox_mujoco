# starrobox_mujoco

MuJoCo models of the Starrobox cells: robot arms (Fairino3/5, MZ07), grippers, cameras and booth enclosures.

- `envs/` holds complete scenes. Open these.
- `models/` holds parts that the scenes include. Some parts, such as `models/box/nakanishi_box.xml`, only load from inside a scene because they inherit its `meshdir`.
- `assets/meshes/` holds the STL and OBJ meshes.

## Setup

`requirements.txt` pins `mujoco==3.3.5`. That release ships wheels for Python 3.9 to 3.13, not 3.14, so create the env with Python 3.12.

With conda (no root needed):

```sh
conda create -y -p ./venv python=3.12
venv/bin/pip install -r requirements.txt
```

Or with the system Python, if `python3.12-venv` is installed:

```sh
python3.12 -m venv venv
venv/bin/pip install -r requirements.txt
```

`venv/` is gitignored.

## Check the scenes

```sh
venv/bin/python scripts/check_models.py
```

This compiles every scene in `envs/` and steps it 100 times. It exits non-zero if any scene fails. To check specific files, pass their paths as arguments.

## View a scene

```sh
venv/bin/python -m mujoco.viewer --mjcf=envs/starrobox_cafe_completed.xml
```
