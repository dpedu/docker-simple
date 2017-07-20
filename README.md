The conf dir (-v /host/conf:/srv/acme/conf/) needs:

    <domain>.com/email    email address to use for the cert request
    <domain>.com/aliases  all hostnames INCLUDING <domain> for cert request

The webroot should be mounted to the real webhost's acme-challenge dir, like:

    -v /host/real_webroot/.well-known/acme-challenge/:/srv/acme/webroot/.well-known/acme-challenge/

Master process logs in /srv/acme/logs/ are useful for debugging

The certs (and account.json) will be placed in /srv/acme/certs/
