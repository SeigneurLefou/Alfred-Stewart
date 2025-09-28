def ft_user_command(subparsers):
	parser_add_2_number = subparsers.add_parser("add_2_number", help="Add two number and print result")
	parser_add_2_number.add_argument("--num1", type=int, required = True)
	parser_add_2_number.add_argument("--num2", type=int, required = True)
	return subparsers