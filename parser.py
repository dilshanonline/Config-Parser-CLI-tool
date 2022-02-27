import os
import sys

import yaml


def get_configs_from_file(file):
    with open(file, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config


def get_configs_from_env(config):
    for key in config:
        uppercase_key = str.upper(key)
        if os.getenv(uppercase_key) is not None:
            config[key] = os.getenv(uppercase_key)
    return config


def get_configs_from_cli(all_args, config):
    for arg in all_args:
        if arg.startswith("--"):
            trimmed_arg = arg.strip()
            trimmed_arg_split = trimmed_arg.split('=')
            arg_key = trimmed_arg_split[0].replace("--", "")
            arg_value = trimmed_arg_split[1]

            arg_key_underscore_case = arg_key.replace("-", "_")

            if arg_key != "config" and arg_key_underscore_case in config and arg_value is not None:
                config[arg_key_underscore_case] = arg_value
    return config


def print_yaml(config):
    print(yaml.dump(config))


def get_config_file_path(all_args, config_arg):
    for arg in all_args:
        trimmed_arg = arg.strip()
        if arg.startswith('--{}'.format(config_arg)):
            return trimmed_arg.split('=')[1]
    return None


all_cli_args = sys.argv[1:]

config_file = get_config_file_path(all_cli_args, "config")
if config_file is not None and os.path.exists(config_file):
    base_config = get_configs_from_file(config_file)
else:
    base_config = {}

base_config = get_configs_from_env(base_config)
base_config = get_configs_from_cli(all_cli_args, base_config)

print_yaml(base_config)
