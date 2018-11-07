CF-Kit
======

# Configuration of Credentials

You need to create a file in you home ```.cloudflare/cloudflare.cfg``` with the following format including your account secrets:

```
[CloudFlare]
email = user@domain.com
token = <FILL_WITH_YOUR_TOKEN>
certtoken =
extras =
```

# Installation with pip

```
pip install git+https://github.com/idontdomath/cf-kit
```

# Development

Feel free to use virtualenv.
if you have pip, just get in the directory and do:

```
pip install --editable .
```

# Usage

just a simple:

```
cf-kit --help
```

will give you hand.
