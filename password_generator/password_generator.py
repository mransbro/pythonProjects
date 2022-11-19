import secrets
import argparse
import string

arg_desc = '''\
        Password generator. Uses secrets module to provides access to the most
        secure source of randomness that your operating system provides.
        '''
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=arg_desc
    )

parser.add_argument("-l",
                    "--length",
                    default=12,
                    type=int,
                    help="Length of the password")

parser.add_argument("-s",
                    "--symbols",
                    action="store_true",
                    help="Exclude symbols from the password")

args = vars(parser.parse_args())

letters = list(string.ascii_letters)
nums = [str(num) for num in range(10)]
symbols = list(string.punctuation)

allchars = {
    1: letters,
    2: nums,
    3: symbols
}

if args["symbols"]:
    choices = [1, 2, 3]
else:
    choices = [1, 2]

password = ''

for item in range(int(args["length"])):
    type = secrets.choice(choices)
    password += secrets.choice(allchars[secrets.choice(choices)])

print(password)
