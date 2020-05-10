class CraftParser:
  @staticmethod
  def calculate_mass(craft_filepath: str, masses: dict) -> int:
    parts = []
    with open(craft_filepath) as craft:
      for line in craft:
        if "part = " in line:
          partname = line.split()[2].split('_')[0]
          parts.append(partname)
    
    mass = 0
    for part in parts:
      print(masses[part])
      mass += masses[part]

    return mass