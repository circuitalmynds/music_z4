from pathlib import Path
from json import load, dumps
jsonconfig = dict(
    indent=4,
    sort_keys=True,
    ensure_ascii=True
)
path = Path(__file__).parent
giturl = "https://github.com/circuitalmynds/music_z4"
folder_content = path.joinpath("videos")
info = path.joinpath("info.json")


def getinfo():
    return load(info.open())


def save_info(data):
    info.open("w").write(dumps(
        data, **jsonconfig
    ))


def getfiles():
    urlfile, totalsize, content = f"{giturl}/blob/main/videos", 0.0, []
    files = list(
        fi for fi in folder_content.iterdir()
        if fi.name != ".nothing" and fi.name.endswith(".mp4")
    )
    for file in files:
        filename = file.name
        size, file_id = file.stat().st_size * 1.0e-6, filename.split(".mp4")[0][-11:]
        content.append(dict(
            name=filename,
            id=file_id,
            size=size,
            path=str(file),
            url=f"{urlfile}/{filename}?raw=true"
        ))
        totalsize += size
    return dict(
        content=content,
        total_size=totalsize,
        available_space=totalsize < 9.5e2
    )


if __name__ == "__main__":
    save_info(getfiles())
    print(getinfo())

