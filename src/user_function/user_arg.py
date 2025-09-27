from export_function import *
def ft_user_arg(args):
	if args.command == "add_two_number":
		add_two_number(args.num1, args.num2)
	return args