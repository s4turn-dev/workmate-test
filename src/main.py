from argparse import ArgumentParser

from command_parser import CommandParser
from custom_csv import CSV

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('--file', required=True)
    argparser.add_argument('--aggregation')
    argparser.add_argument('--where')
    argparser.add_argument('--order-by')
    args = argparser.parse_args()

    cmdparser = CommandParser(args)

    csv = CSV()
    csv.load_from_file(args.file)

    if args.aggregation:
        csv.aggregate(*cmdparser.aggregation)

    if args.where:
        csv.filter(*cmdparser.filter)

    if args.order_by:
        csv.order_by(*cmdparser.order_by)
    
    print(csv)
