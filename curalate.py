#!/usr/bin/env python

import argparse
import sys
import subprocess

RESERVED = {
    "update": 'CuralateUpdate'
}


class CuralateExecution:
    def __init__(self, service, subcommand, options):
        self._service = service
        self._subcommand = subcommand
        self._options = options

    def process(self):
        if self._service in RESERVED.keys():
            getattr(RESERVED[self._service],'__init__')()


class CuralateCommand:
    def __init__(self, service, subcommand, options):
        self.service = service
        self._subcommand = subcommand
        self._options = options

    @property
    def subcommand(self):
        return self._subcommand

    def run(self):
        return subprocess.check_call([self._subcommand] + self._options)


class CuralateUpdate(CuralateCommand):
    def __init__(self):
        CuralateCommand.__init__(self, 'update', 'brew', [''])
        print (subprocess.check_call(['git', 'pull']))


def handle_service(service_name=None):
    if service_name is None:
        print (subprocess.check_call(['ls']))
        return 0
    assert isinstance(service_name, str)
    if service_name.lower() == 'update':
        CuralateUpdate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Curalate dev tools')

    parser.add_argument('service', action="store", type=str)
    parser.add_argument('command', action="store")
    parser.add_argument('options', nargs='*', type=str)
    parser.parse_known_args(['service', 'command'])

    if len(sys.argv) == 2:
        sys.argv = sys.argv + ['run']

    # Add '--' to indicate to argparse that subsequent strings are not flags
    sys.argv = sys.argv[:3] + ['--'] + sys.argv[3:]

    args = parser.parse_args()
    print (args)

    # cura_command = CuralateCommand(service=args.service, subcommand=args.command, options=args.options)
    exe = CuralateExecution(service=args.service, subcommand=args.command, options=args.options)
    exe.process()
    handle_service(args.service)
    # print (cura_command.run())
