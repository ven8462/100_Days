#!/usr/bin/python3

import cmd

class MyConsole(cmd.Cmd):
    prompt = "AirBnB$ "
    
    def parseline(self, line):
        print('parseline({!r}) =>'.format(line), end='')
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret
    
    
    def onecmd(self, s):
        print('onecmd({})'.format(s))
        return cmd.Cmd.onecmd(self, s)
    
    def default(self, line):
        print('default({})'.format(line))
        return cmd.Cmd.default(self, line)

    
    
    def emptyline(self):
        print('emptyline()')
        return cmd.Cmd.emptyline(self)
    
    def precmd(self, line):
        print('precmd({})'.format(line))
        return cmd.Cmd.precmd(self, line)

    def do_EOF(self, line):
        """exits the program"""
        print(line)
        return True
    
    def do_greet(self, person):
        """greets user"""
        if person:
            print("hello", person)
        else:
            print("hello")

if __name__ == "__main__":
    MyConsole().cmdloop()