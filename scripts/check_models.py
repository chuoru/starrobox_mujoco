import sys
from pathlib import Path

import mujoco

ROOT = Path(__file__).resolve().parent.parent
STEPS = 100


def check(path: Path) -> str | None:
    try:
        model = mujoco.MjModel.from_xml_path(str(path))
        data = mujoco.MjData(model)
        mujoco.mj_step(model, data, nstep=STEPS)
    except Exception as e:
        return str(e).strip().splitlines()[0]
    return None


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]] or sorted((ROOT / "envs").glob("*.xml"))
    failures = 0
    for path in paths:
        error = check(path)
        failures += error is not None
        print(f"{'FAIL' if error else 'ok  '} {path.relative_to(ROOT) if path.is_absolute() else path}"
              + (f"  {error}" if error else ""))
    print(f"mujoco {mujoco.__version__}: {len(paths) - failures}/{len(paths)} loaded and stepped {STEPS} times")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
