import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from parts_parser import PartsParser # pylint: disable=import-error
from craft_parser import CraftParser # pylint: disable=import-error

def setup_arguments():
  parser = argparse.ArgumentParser()
  # parser.add_argument("craft", help="Path to craft file")
  # parser.add_argument("ksp_gamedata", help="Path to GameData folder of KSP install")

  return parser.parse_args()


def main():
  # args = setup_arguments()
  # masses = PartsParser.parse_masses(args.ksp_gamedata)
  # PartsParser.save_masses(masses, 'stockmasses.json')
  masses = PartsParser.load_masses('stockmasses.json')
  dist = CraftParser.calculate_mass_distribution_3d('example_crafts\\Aeris 3A.craft', masses)
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(xs=[item[1][0] for item in dist], ys=[item[1][1] for item in dist],
    zs=[item[1][2] for item in dist], s=[100* 2**item[0] for item in dist], depthshade=False)
  
  plt.show()
  # print(masses)


if __name__ == '__main__':
  main()