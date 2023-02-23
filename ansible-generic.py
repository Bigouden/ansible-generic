#!/usr/bin/env python3
#coding: utf-8

import argparse
import os
import ansible.cli.doc
from ansible import context

PARSER = argparse.ArgumentParser(description="Template Generic Ansible Loop Task.")
PARSER.add_argument('module', help='Ansible Module')
ARGS = PARSER.parse_args()
CLIARGS = {'version': None,
           'verbosity': 0,
           'module_path': None,
           'basedir': None,
           'args': ('ansible.builtin.template',),
           'type': 'module',
           'json_format': True,
           'entry_point': None,
           'show_snippet': False,
           'list_files': False,
           'list_dir': False,
           'dump': False,
           'no_fail_on_errors': False}

def main():
    ''' Get Ansible Module Documentation & Generate Generic Ansible Loop Tasks'''
    doc = ansible.cli.doc.DocCLI(ARGS)
    module = (ARGS.module,)
    CLIARGS['args'] = module
    context.CLIARGS = CLIARGS
    try:
        unorder_module_options = dict((doc._get_plugins_docs('module', module)[ARGS.module]['doc']['options']))
        order_module_options = dict(sorted(unorder_module_options.items()))
        print(f'- name: Common Task For {ARGS.module}') 
        print(f'  {ARGS.module}:') 
        for key, value in order_module_options.items():
            if 'required' in value and value['required']:
                print(f'    {key}: "{{{{ item.{key} }}}}"')
            else:
                print(f'    {key}: "{{{{ item.{key} | default(omit) }}}}"')
        print('  loop: "{{ variable }}"')
        print('  when:')
        print('    - variable is defined')
        print('    - variable | length > 0')
    except KeyError:
        os._exit(1)

if __name__ == '__main__':
    main()
