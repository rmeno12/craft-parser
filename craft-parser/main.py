import argparse
from parts_parser import PartsParser # pylint: disable=import-error
from craft_parser import CraftParser # pylint: disable=import-error

def setup_arguments():
  parser = argparse.ArgumentParser()
  # parser.add_argument("craft", help="Path to craft file")
  # parser.add_argument("ksp_gamedata", help="Path to GameData folder of KSP install")

  return parser.parse_args()


def main():
  args = setup_arguments()
  # masses = PartsParser.parse_masses(args.ksp_gamedata)
  # PartsParser.save_masses(masses, 'stockmasses.json')
  masses = PartsParser.load_masses('stockmasses.json')
  print(CraftParser.calculate_mass('example_crafts\\Aeris 3A.craft', masses))
  # print(masses)


if __name__ == '__main__':
  main()