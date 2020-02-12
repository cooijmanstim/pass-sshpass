import os, subprocess as sp, argparse

parser = argparse.ArgumentParser(description="ssh with password persistence.")
parser.add_argument("path", help="path into the `pass` tree, e.g. example.com/ssh")
args, command = parser.parse_known_args()

rpipe, wpipe = os.pipe()
os.set_inheritable(rpipe, True)
os.set_blocking(wpipe, False)

sp.check_call(["pass", "show", args.path], stdout=wpipe)
os.close(wpipe)

os.execvp("sshpass", ["sshpass", "-d%i" % rpipe] + command)
