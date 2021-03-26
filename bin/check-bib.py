#!/usr/bin/env python

'''Check consistency of bibliography definitions and references.'''

import argparse
import re
import sys

import utils


# Pattern that keys must match.
KEY = re.compile(r'^[A-Za-z]+\d{4}[a-z]?$')

def check_bib(options):
    '''Main driver.'''
    config = utils.read_yaml(options.config)
    filenames = [entry['file'] for entry in utils.get_entry_info(config)]
    defined = get_definitions(options.bibliography)
    check_order(defined)
    check_keys(defined)
    cited = utils.get_all_matches(utils.CITATION, filenames)
    utils.report('bibliography', cited=cited, defined=set(defined))


def get_definitions(filename):
    '''Create set of citation keys.'''
    def _key(entry):
        assert 'key' in entry, f'Entry {entry} missing "key"'
        return entry['key']
    raw = utils.read_yaml(filename)
    return [_key(entry) for entry in raw]


def check_order(keys):
    '''Make sure keys are in order.'''
    previous = None
    unordered = []
    for key in keys:
        if previous is not None:
            if key.lower() < previous.lower():
                unordered.append(key)
        previous = key
    if unordered:
        print('- bibliography order')
        for key in unordered:
            print(f'  - {key}')


def check_keys(keys):
    '''Make sure all keys are name + 4-digit year.'''
    bad_keys = [k for k in keys if not KEY.match(k)]
    if bad_keys:
        print('- bibliography keys')
        for k in bad_keys:
            print(f'  - {k}')


if __name__ == '__main__':
    options = utils.get_options(
        ['--bibliography', False, 'Path to bibliography YAML file'],
        ['--config', False, 'Path to YAML configuration file']
    )
    check_bib(options)
