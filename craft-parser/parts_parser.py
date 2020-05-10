from pathlib import Path
import json

class PartsParser:
  @staticmethod
  def parse_masses(filepath: str) -> dict:
    masses = {}
    cfgs = list(Path(filepath + "\\Squad\\Parts").rglob("*.cfg"))
    for cfg in cfgs[1:]:
      name = ''
      mass = -1
      with cfg.open() as f:
        for line in f:
          if 'name' in line.split() and name == '':
            for index, word in enumerate(line.split()):
              if word == '=':
                name = line.split()[index+1].strip(' \n\t=')
                break
              elif len(word) > 1 and word[0] == '=':
                name = word.strip(' \n\t=')
                break
          
          if 'mass' in line.split() and mass == -1:
            for index, word in enumerate(line.split()):
              if word == '=':
                mass = float(line.split()[index+1].strip(' \n\t='))
                break
              elif len(word) > 1 and word[0] == '=':
                mass = float(word.strip(' \n\t='))
                break

          if name != '' and mass != -1:
            break
      
      if name != '' and mass != -1:
        masses[name] = mass

    return masses

  @staticmethod
  def save_masses(masses: dict, filename: str):
    json.dump(masses, Path(filename).open(mode='w'), indent="\t")

  @staticmethod
  def load_masses(filename: str) -> dict:
    masses = json.load(Path(filename).open(mode='r'))

    return masses
