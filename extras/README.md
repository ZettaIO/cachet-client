
# Extras

Contains simple live testing and release instructions.

## Live Tests

This is a simple module doing some quick sanity checking using
and actual cachet service.

* Start up cachet using the docker-compose setup in the project root
  * Should have cachet 2.3 and 2.4 with separate databases
  * You may need to commend out the API_TOKEN on first run and
    fetch the generated one in your local cachet service on first startup.
* Edit `env23.sh` and `env24.sh` with your own API tokens
* Run `live_run.py` with each environment.

Environment variables for `live_run.py`:

```bash
CACHET_ENDPOINT
CACHET_API_TOKEN
```
