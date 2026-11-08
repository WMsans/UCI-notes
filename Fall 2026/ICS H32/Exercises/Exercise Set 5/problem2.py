import requests

START_LOCATION = "start.dat"

class Dat:
    location = ""
    title = ""
    description = ""
    commands = []
    game_over = False

    def parse_dat(self, dat_file: str) -> str:
        lines = dat_file.splitlines()
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]
            stripted_line = line.strip()
            if stripted_line.startswith("TITLE"):
                self.title = stripted_line[len("TITLE"):].strip()
                i += 1
            
            elif stripted_line.startswith("DESCRIPTION"):
                desc_lines = []
                i += 1
                while i < n and lines[i].strip() != "END DESCRIPTION":
                    desc_lines.append(lines[i])
                    i += 1
                self.description = '\n'.join(desc_lines)
                i += 1
            elif stripted_line.startswith("COMMANDS"):
                i += 1
                while i < n and lines[i].strip() != "END COMMANDS":
                    entry = lines[i].strip()
                    if entry:
                        aliases_part, _, dest = entry.partition(":")
                        aliases = [a.strip().upper() for a in aliases_part.split(",") if a.strip()]
                        self.commands.append((aliases, dest.strip()))
                    i += 1
                i += 1

            elif stripted_line.startswith("GAME OVER"):
                self.game_over = True
                i += 1

            else:
                i += 1
    
    def render_scene(self, show_description: bool) -> None:
        print(self.title)
        if show_description:
            print(self.description)

    def game_action(self) -> str:
        action: str = input("Please input your action: ").strip().upper()
        for i in self.commands:
            aliases, dest = i
            for j in aliases:
                if action == j:
                    return dest
        raise ValueError(action)

    def fetch_url(self, url: str) -> str:
        response = requests.get(url)
        response.raise_for_status()
        return response.text


    def __init__(self, base_url:str, current_location: str) -> None:
        self.location = current_location
        self.commands = []  # per-instance; a shared class list leaks commands across locations
        self.parse_dat(self.fetch_url(base_url + current_location))

def main():
    base_url = input("Please input the base url:")
    base_url = base_url + "/" if not base_url.endswith("/") else base_url
    current_location = START_LOCATION
    visited = set()

    # Game loop
    while(True):
        dat_file = Dat(base_url, current_location)
        dat_file.render_scene(current_location not in visited)
        visited.add(current_location)
        if dat_file.game_over:
            return
        
        successed = False
        while not successed:
            try:
                new_dest = dat_file.game_action()
                current_location = new_dest + ".dat"
                successed = True
            except ValueError:
                print("Invalid command. Try again.")


if __name__ == "__main__":
    main()
