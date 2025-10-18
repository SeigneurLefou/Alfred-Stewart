def ft_user_command(subparsers):

	parser_echo_function = subparsers.add_parser("echo_function", help="print function")
	parser_echo_function.add_argument("--text", type=str, required = True)

	parser_echo_function = subparsers.add_parser("echo_function", help="print function")
	parser_echo_function.add_argument("--text", type=str, required = True)
	return subparsers