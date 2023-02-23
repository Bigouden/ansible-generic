# ansible-generic

## Description

Permet de générer une tâche générique avec boucle à partir des informations founis par la documentation ansible.

## Prérequis

- python 3
- ansible-core

## Utilisation 

### Aide

```bash
ansible-generic -h

usage: ansible-generic [-h] module

Template Generic Ansible Loop Task.

positional arguments:
  module      Ansible Module

options:
  -h, --help  show this help message and exit
```

### Module

```bash
ansible-generic <module>
```

## Exemple

![exemple d'utilisation](example.gif "Example")
