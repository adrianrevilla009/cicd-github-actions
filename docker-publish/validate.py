"""Parse every YAML file in this folder and check the minimum GitHub Actions shape."""
import json, pathlib, sys, yaml

bad = 0
for p in sorted(pathlib.Path(__file__).parent.rglob("*.y*ml")):
    doc = yaml.safe_load(p.read_text())
    if not isinstance(doc, dict):
        print(f"FAIL {p.name}: not a mapping"); bad += 1; continue
    kind = "workflow" if "jobs" in doc else "action" if "runs" in doc else "config"
    # PyYAML parses the bare key `on` as True
    if kind == "workflow" and not ("on" in doc or True in doc):
        print(f"FAIL {p.name}: workflow without trigger"); bad += 1; continue
    perms = doc["jobs"]["image"]["permissions"]
    if perms.get("packages") != "write": print("FAIL packages: write missing"); bad += 1

    print(f"ok   {p.name} ({kind})")
sys.exit(1 if bad else 0)
