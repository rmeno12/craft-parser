class CraftParser:
  @staticmethod
  def calculate_mass(craft_filepath: str, masses: dict) -> int:
    parts = []
    craft_lines = []
    with open(craft_filepath) as craft:
      craft_lines = [line.strip() for line in craft.readlines()]
    
    for index, line in enumerate(craft_lines):
      if "part = " in line:
        # Replacing period with underscore because in craft files some parts 
        # are stored with periods even though their names in cfg files 
        # use underscores
        partname = line.split()[2].split('_')[0].replace('.', '_')
        parts.append((partname, 1))
      elif 'RESOURCE' in line:
        resourcename = craft_lines[index + 2].split()[2]
        amount = float(craft_lines[index + 3].split()[2])
        parts.append((resourcename, amount))
    
    mass = 0
    for part in parts:
      mass += masses[part[0]] * part[1]

    return mass