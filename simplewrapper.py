#!/usr/bin/env python3

from subprocess import Popen, TimeoutExpired
import os


CONF_DIR = "/srv/acme/conf/"
WEB_ROOT = "/srv/acme/webroot/"


def main():
    for name in os.listdir(CONF_DIR):
        domain_dir = os.path.join(CONF_DIR, name)
        with open(os.path.join(domain_dir, "email")) as f:
            email = f.read().strip()
        with open(os.path.join(domain_dir, "aliases")) as f:
            aliases = [i.strip() for i in f.read().strip().split()]

        call_le(email, aliases, domain_dir)


def call_le(email, domain_names, cwd):
    assert domain_names
    os.chdir(cwd)

    le_call = ["simp_le",
               "--email", email,
               "-f", "account_key.json",
               "-f", "fullchain.pem",
               "-f", "key.pem"]

    for domain in domain_names:
        le_call += ["-d", domain]

    le_call += ["--default_root", WEB_ROOT]

    p = Popen(le_call)
    try:
        p.wait(30)
    except TimeoutExpired:
        p.kill()

    if p.returncode == 0:
        print("renewed {}".format(domain_names[0]))
    elif p.returncode == 1:
        print("no renew needed for {}".format(domain_names[0]))
    elif p.returncode == 2:
        print("error updating {}1".format(domain_names[0]))


if __name__ == '__main__':
    main()
