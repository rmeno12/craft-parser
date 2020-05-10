import argparse
from parts_parser import PartsParser # pylint: disable=import-error

def setup_arguments():
  parser = argparse.ArgumentParser()
  # parser.add_argument("craft", help="Path to craft file")
  parser.add_argument("ksp_gamedata", help="Path to GameData folder of KSP install")

  return parser.parse_args()


def main():
  args = setup_arguments()
  masses = PartsParser.parse_masses(args.ksp_gamedata)

  print(masses)


if __name__ == '__main__':
  main()