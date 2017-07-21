import sys

from simulator import Simulator


def usage(args):
    print("{} <num-elevators> <num-floors>".format(args[0]))


def main(args):
    num_elevators = 4
    if len(args) >= 3:
        num_elevators = int(args[1])
        num_floors = int(args[2])
    else:
        usage(args)
        exit(1)

    simulator = Simulator(num_elevators, num_floors)
    simulator.run()


if __name__ == "__main__":
    main(sys.argv)
