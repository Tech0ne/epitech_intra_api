# Epitech Intra API

---

Used to interact with the intranet of EPITECH.

---

## Installation

For now, run your python script on this folder, and import epitech_intra_api (the folder) to use.

In a near future, this lib will be available on Pypi, so you will just need to `pip3 install epitech_intra_api`

---

## Usage

```py
from epitech_intra_api import *

client = Client("<login token (the user cookie of intra.epitech.eu)>")
```

---

## TODOs

- [ ] Request `/module/{year}/{module}/{city}/{activity}`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/note`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/note`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/project`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/project/file`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/project/registered`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/rdv`
- [ ] Request `/module/{year}/{city}/{activity}/project/confirmjoingroup`
- [ ] Request `/module/{year}/{city}/{activity}/project/confirmleavegroup`
- [ ] Request `/module/{year}/{city}/{activity}/project/declinejoingroup`
- [ ] Request `/module/{year}/{city}/{activity}/project/destroygroup`
- [ ] Request `/module/{year}/{module}/{city}/{activity}/project/register`
- [ ] Request `/module/{year}/{city}/{activity}/project/unregister`
- [ ] Request `/module/{year}/{module}/{city}`
- [ ] Request `/module/{year}/{module}/{city}/registered`
- [ ] Request `/filter`
- [ ] Request `/planning/load`
- [ ] Request `/planning/my-schedules`
- [x] Request `/user/{user}`
- [x] Request `/user/{user}/binome`
- [ ] Request `/user/{user}/flags`
- [ ] Request `/user/{user}/marks`
- [ ] Request `/user/{user}/netsoul`
- [ ] Request `/user/{user}/notification/{type}`
- [ ] Request `/user/{user}/print`
- [ ] Request `/`
- [ ] Request `/file/{directory}`
- [ ] Complete README

_based on https://cyberryteam.github.io/epitech-intranet-api/_