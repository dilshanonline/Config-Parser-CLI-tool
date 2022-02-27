# Config-Parser-CLI-tool
## Purpose
-   This config parser should do the following:
    -   Accept an optional argument`--config` for a config file
    -   Accept optional arguments for fields in the config file
    -   Handle environment variables
    -   Precedence should operate: `cli > environment > config file`
-   It build out a valid config and print out a yaml file for the final config.

## Usage

### Run file
  `$ python3 parser.py --config=config.yaml`

### Override via environment variables, *DB HOST*

    $ export DB_HOST=localhost:5454
    $ python3 parser.py --config=config.yaml

### Override via environment variables, *DB Password*

    $ export DB_PASSWORD=blah 
    $ python3 parser.py --config=config.yaml

### Override via CLI

    $ python3 parser.py --config=config.yaml --db-host=remote:5460
    $ python3 parser.py --config=config.yaml

