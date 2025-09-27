def ft_user_command(subparsers):
	parser_add_two_number = subparsers.add_parser("add_two_number")
	parser_add_two_number.add_argument("--num1", required = True)
	parser_add_two_number.add_argument("--num2", required = True)
	return subparsers