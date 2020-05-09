import argparse


def setup_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("craft", help="Path to craft file")

  return parser.parse_args()
  

def main():
  args = setup_arguments()
  print('main')


if __name__ == '__main__':
  main()