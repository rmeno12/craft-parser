import argparse
from parts_parser import PartsParser # pylint: disable=import-error

def setup_arguments():
  parser = argparse.ArgumentParser()
  # parser.add_argument("craft", help="Path to craft file")
  parser.add_argument("ksp_gamedata", help="Path to GameData folder of KSP install")

  return parser.parse_args()


def main():
  args = setup_arguments()
  parts_parser = PartsParser()
  masses = parts_parser.parse_masses(args.ksp_gamedata).masses
  # parts_parser.save_masses('testout.json')
  # print(args.ksp_gamedata)


if __name__ == '__main__':
  main()