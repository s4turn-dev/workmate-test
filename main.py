from custom_argparser import CustomArgumentParser
from custom_csv import CSV



if __name__ == '__main__':
    parser = CustomArgumentParser()
    args = parser.parse_args()
    print(args)

    if args.aggregation:
        aggr = parser.parse_aggregation()
        print(aggr)

    if args.where:
        filter = parser.parse_filter()
        print(filter)

    if args.order_by:
        order = parser.parse_order_by()
        print(order)
