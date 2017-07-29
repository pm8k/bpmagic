from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic)
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
import os


def check_directory():
    userpath = os.path.expanduser('~')
    dirpath = "{UP}/.bpmagic".format(UP=userpath)
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

# Main Magic Class


@magics_class
class BPMagic(Magics):

    # function to load one or more modules into an ipython cell
    @magic_arguments()
    @argument('arg', nargs='*', action='append')
    @line_magic
    def iload(self, arg):
        args = parse_argstring(self.iload, arg).arg[0]

        if len(args) == 0:
            ValueError('No arguments passed to %iload')
        linelist = []
        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)
        for arg in args:
            filepath = "{DP}/{PROF}.py".format(PROF=arg, DP=dirpath)
            if not os.path.isfile(filepath):
                raise ValueError(
                    'No bpmagic file named {PROF}. Use %ilist to list all profiles.'.format(PROF=arg))
            file = open(filepath, 'r')
            lines = file.read()
            lines = '#' + arg + '\n' + lines
            linelist.append(lines)
            file.close()
        alllines = '\n\n'.join(linelist)
        self.shell.set_next_input(alllines, replace=True)

        # self.shell.ex(alllines)

    # load all saved chunks into a single cell
    # anyway to load 'groups' of cells? any use?
    @line_magic
    def iloadall(self, arg):
        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)
        names = os.listdir(dirpath)

        if len(names) == 0:
            ValueError('No profiles to load, save profiles first using %isave')
        linelist = []
        for arg in names:
            filepath = "{DP}/{PROF}.py".format(PROF=arg, DP=dirpath)

            file = open(filepath, 'r')
            lines = file.read()
            lines = '#' + arg + '\n' + lines
            linelist.append(lines)
            file.close()
        alllines = '\n\n'.join(linelist)
        self.shell.set_next_input(alllines, replace=True)

    # save everything in the current cell to the name of the profile
    # if overwriting a previously defined profile use -o or --overwrite
    @magic_arguments()
    @argument('profile', nargs=1, action='append')
    @argument('--overwrite', '-o', action='store_true')
    @cell_magic
    def isave(self, line, cell=None, local_ns=None):

        # ensure there is a .imports dire
        check_directory()
        args = parse_argstring(self.isave, line)
        profile = args.profile[0][0]
        # TODO: Check charstring of filename to see if it can be written
        overwrite = args.overwrite
        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)
        filepath = "{DP}/{PROF}.py".format(PROF=profile, DP=dirpath)

        if overwrite is not True:
            if os.path.isfile(filepath):
                print 'here'
                raise ValueError(
                    'Already Exists, use -o or --overwrite to overwrite file')
        file = open(filepath, "w")
        file.write(cell)
        file.close()

    # list every profile currently saved
    @line_magic
    def ilist(self, line):

        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)

        names = os.listdir(dirpath)
        names = [x[:-3] for x in names]
        for n in names:
            print n

    # TODO: See if you can add run functionality to iload

    # delete the named profile
    @magic_arguments()
    @argument('arg', nargs='*', action='append')
    @line_magic
    def idelete(self, arg):
        args = parse_argstring(self.idelete, arg).arg[0]

        if len(args) == 0:
            ValueError('No arguments passed to %idelete')
        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)
        filepath = "{DP}/{PROF}.py".format(PROF=arg, DP=dirpath)
        if not os.path.isfile(filepath):
            raise ValueError(
                'No bpmagic file named {PROF}. Use %ilist to list all profiles.'.format(PROF=arg))
        else:
            os.remove(filepath)
            print 'Profile {PROF} has been deleted'.format(PROF=arg)

    # rename profile from one name to another
    @magic_arguments()
    @argument('oldprofile', nargs=1, action='append')
    @argument('newprofile', nargs=1, action='append')
    @argument('--overwrite', '-o', action='store_true')
    @line_magic
    def irename(self, line):

        # ensure there is a .imports dire
        check_directory()
        args = parse_argstring(self.irename, line)
        userpath = os.path.expanduser('~')
        dirpath = "{UP}/.bpmagic".format(UP=userpath)
        oldprofile = args.oldprofile[0][0]
        newprofile = args.newprofile[0][0]

        oldfilepath = "{DP}/{PROF}.py".format(PROF=oldprofile, DP=dirpath)
        if not os.path.isfile(oldfilepath):
            raise ValueError(
                'No bpmagic file named {PROF}. Use %ilist to list all profiles.'.format(PROF=arg))

        # TODO: Check charstring of filename to see if it can be written
        overwrite = args.overwrite
        newfilepath = "{DP}/{PROF}.py".format(PROF=newprofile, DP=dirpath)

        if overwrite is not True:
            if os.path.isfile(newfilepath):
                print 'here'
                raise ValueError(
                    'Already Exists, use -o or --overwrite to overwrite file')
        os.rename(oldfilepath, newfilepath)


ip = get_ipython()

ip.register_magics(BPMagic)

# In order to actually use these magics, you must register them with a
# running IPython.  This code must be placed in a file that is loaded once
# IPython is up and running:
# You can register the class itself without instantiating it.  IPython will
# call the default constructor on it.


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(BPMagic)
