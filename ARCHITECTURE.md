# Project architecture

## Directories and files

The project structure applies both for development and production:

- The project directory contains two subdirectories: `bin` and
  `libexec`.

    ```plain
    hello-world
    ├── bin
    └── libexec
    ```

- Your code goes into `*.bash` scripts inside the `libexec` directory.

    ```plain
    hello-world
    ├── bin
    └── libexec
        └── hello.bash
    ```

- To prevent shadowing existing shell functions that you may have
  in your shell’s scope already, every function in your project
  starts with a `__` prefix.

    ```bash
    # hello.bash
    function __hello {
      echo 'Hello, world!'
    }

    export -f __hello
    ```

- To `source` one of your `*.bash` script into another, you can
  use a relative path, e. g.:

    ```bash
    # hello.bash
    source libexec/constants.bash

    function __hello {
      echo "${__HELLO}"
    }

    export -f __hello
    ```

    ```bash
    # constants.bash
    __HELLO='Hello, world!'
    ```

- Each executable command is represented by a stub in the `bin`
  directory. This stub is called the _internal stub._  
  For details, refer to the _Content of the internal stub_ section.

    ```plain
    hello-world
    ├── bin
    │   └── hello
    └── libexec
        ├── constants.bash
        └── hello.bash
    ```

- For each executable command, the `*.bash` script contains a main
  function. Derive the function name from the command name using the
  following rule:
  Take the command name, add a `__` prefix, then replace every
  sequence of characters not in `[A-Za-z0-9_]` by a single `_`.

    ```plain
    rename-partition
    ├── bin
    │   └── rename-partition.fat32
    └── libexec
        └── rename-partition.fat32.bash
    ```

    ```bash
    # rename-partition.fat32.bash

    function __rename_partition_fat32 {
      […]
    }
    ```

- For packaging, you typically add a second shim, the _external stub._  
  For details, see the _Content of the external stub_ section.

    ```plain
    /
    └── usr
        ├── bin
        │   └── hello                   ← External stub
        └── lib
            └── hello-world
                ├── bin
                │   └── hello           ← Internal stub
                └── libexec
                    ├── constants.bash
                    └── hello.bash      ← Actual code
    ```

## Content of the internal stub

The internal stub for each executable command looks like this:

```plain
hello-world
├── bin
│   └── hello               ← Internal stub
└── libexec
    └── …
```

```bash
#!/bin/bash
set -eu -o pipefail
pushd "$(dirname -- "${BASH_SOURCE[0]}")/.." > /dev/null
BASENAME="$(basename -- "${BASH_SOURCE[0]}")"

# shellcheck disable=SC1090
source "libexec/${BASENAME}.bash"

popd > /dev/null
shopt -s extglob
__"${BASENAME//+([^a-z0-9_])/_}" "$@"
```

The internal stub works by `source`-ing a `*.bash` script from
`libexec`, then execute the main function of that script.

I have designed the internal stub with the following design goals
in mind:

- **Packageability:**
  The internal stub must play well with any system package manager.

- **Reusability:**
  The internal stub allows for any (internal or external) code to
  source _any_ `*.bash` script from this package without invoking
  the main function of that script.  
  In other words, the `*.bash` script not only makes the main
  function available to callers, but _all_ of its functions.

- **Resource management:**
  Exporting a shell function means the caller does not need to
  spawn a subshell, but rather execute the function directly.

## Content of the external stub

An example for an external stub for a single executable command
on Arch Linux:

```plain
/
└── usr
    ├── bin
    │   └── hello                   ← External stub
    └── lib
        └── hello-world
            ├── bin
            │   └── hello
            └── …
```

```bash
#!/bin/bash
BASENAME="$(basename "${BASH_SOURCE[0]}")"
exec "/usr/lib/hello-world/bin/${BASENAME}" "$@"
```

The purpose of the external stub is to know where the internal stub
is, and to call it.

External stubs make it easier for a package to have an executable
command link to its backing `*.bash` script. At the same time, it
helps the `*.bash` script maintain stable links to its own
dependencies (i.e. other `*.bash` scripts, which it `source`s
using a relative path).

For other package managers or distributions, adjust the path in the
`exec` line according to where you’re going to put the internal
stub.
