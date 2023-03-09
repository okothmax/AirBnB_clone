#!/usr/bin/env python3

"""
first version of the console
This is the entry point to the commandline interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Handles the 'quit' command

        Args:
            line(args): input argument for quiting
            the terminal

        """
        return True

    def do_EOF(self, line):
        """Quits command interpreter with ctrl+d

         Args:
            line(args): input argument for quiting
            the terminal

        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
