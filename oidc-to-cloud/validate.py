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
    if p.name == "deploy.yml":
        if doc["permissions"].get("id-token") != "write": print("FAIL id-token: write missing"); bad += 1
        if "secrets." in p.read_text(): print("FAIL static secret referenced"); bad += 1
    if p.name.startswith("trust"):
        sub = doc["Statement"][0]["Condition"]["StringEquals"]["token.actions.githubusercontent.com:sub"]
        if "*" in sub or not sub.startswith("repo:"): print("FAIL sub claim not pinned"); bad += 1

    print(f"ok   {p.name} ({kind})")
sys.exit(1 if bad else 0)
