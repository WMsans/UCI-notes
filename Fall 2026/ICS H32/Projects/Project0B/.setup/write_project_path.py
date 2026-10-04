from pathlib import Path
import sysconfig


# Creates an "ics.project.pth" file within the virtual environment, so that all modules in the
# "src" directory are visible without qualification (i.e., a file "person.py" in "src" would be
# importable as "import person", not as "import src.person").


def run() -> None:
    site_packages_path = Path(sysconfig.get_path('purelib'))
    project_path = Path.cwd()
    site_packages_depth = len(site_packages_path.relative_to(project_path).parts)
    relative_src_path = f'{('../' * site_packages_depth)}src'

    with (site_packages_path / 'ics.project.pth').open('w') as project_pth_file:
        project_pth_file.write(f'{relative_src_path}\n')


if __name__ == '__main__':
    run()
