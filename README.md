# pass-sshpass

A Python script to take a password from the [pass](https://www.passwordstore.org) password manager and channel it into [sshpass](https://linux.die.net/man/1/sshpass) via anonymous pipe.

Example usage: `pass-sshpass.py example.com/ssh ssh example.com` will call `pass example.com/ssh`, write its output into an anonymous pipe, and pass the other end of the pipe into `sshpass ssh example.com` using the `-d` flag.
