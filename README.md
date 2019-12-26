# Shorty

This project is part of the FociPy projects. To find out more, checkout [focipy/core](https://github.com/focipy/core) on GitHub.

 - [ ] add to `focpiy/core/future`
 - [ ] create project repository
 - [ ] program completes first pass
 - [ ] update `./README.md` with the startup guide
 - [ ] create a tutorial at `./tutorial/`

## Overview

The program alias `shorty` is a simple name for a url shortener. Shorty commonly describes
a beginner in the field, as this program will cover only basic operations.

### behavior

The user will be able to post new URLs to be shorten. The URLs will be available
indefinitely. In addition, the user can define a custom url. Links are publicly
available.

### decisions

To store the data we need some kind of persistent storage, since runtime memory is
insufficient due to program restarts. Using a database table is an overkill for
such a simple project. Therefore, I'll use Redis to store the info.

### disclosed shortages

The URL management is insufficient for real-world application. A management api
has to be create to manage their urls.

## Startup Guild

`Explain how to use the program from pulling the code to running it.`

### debugging

`Include a short debugging info here.`

# Licence

[MIT](MIT-LICENCE)
