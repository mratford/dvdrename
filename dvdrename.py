def move_to_tv_dir(
    files_directory: Path,
    tv_directory: Path,
    show_name: str,
    series_number: int,
    show_year: int | None = None,
    episode_start: int | None = None
):
    if show_year is not None:
        show_name = f"{show_name} ({show_year})"
    series_directory = tv_directory / show_name / f"Season {series_number:02d}" 
    series_directory.mkdir(parents = True, exist_ok = True)
    new_shows = sorted(files_directory.iterdir())
    if episode_start is None:
        old_shows = sorted(series_directory.iterdir())
        last_episode = max([int(x.stem.split(" - ")[1][-2:]) for x in old_shows], default = 0)
        episode_start = last_episode + 1
    for episode_file in new_shows:
        file_extension = episode_file.suffix
        new_location = series_directory / f"{show_name} - s{series_number:02d}e{episode_start:02d}{file_extension}"
        episode_start += 1
        print(f"Moving {episode_file} to {new_location}")
        episode_file.move(new_location)

