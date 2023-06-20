import requests;
import sys;
from pathlib import Path;

cwd=Path(__file__).parent.absolute()

if "r" in sys.argv:
    res=requests.request("GET", "https://raw.githubusercontent.com/DrFZh/drfzh.github.io/main/_pages/about.md")
    cwd.joinpath("fan.md").write_text(res.text)

if "s" in sys.argv:
    res=cwd.joinpath("fan.md").read_text()
    lines=res.split("\n")
    data=[]
    for line in lines:
        if line.startswith("["):
            data.append(line)

    cwd.joinpath("fan.csv").write_text("\n".join(data))