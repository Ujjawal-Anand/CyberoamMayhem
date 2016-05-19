CyberoamMayhem - perform dictionary attack on Cyberoam web client.

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [USAGE](#usage)
- [OPTIONS](#options)
- [FAQ](#faq)
- [DEVELOPER INSTRUCTIONS](#developer-instructions)
- [COPYRIGHT](#copyright)

# INSTALLATION

Coming soon...

# DESCRIPTION

CyberoamMayhem is a small command-line program to perform brute force attack (dictionary attack precisely, if I say) on Cyberoam Web client. It requires Python interpreter, version 2.6+ (support for version 3.0+ coming soon) and it is not platform specific as long as you have Python and every required packages (mechanize, optparse and others..) installed.It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

# USAGE

    python CyberoamMayhem.py USERNAME Options    

# OPTIONS

    -h,  --help                      Print this help
    -p,  --password_start            Number from which you want to start checking for password 
                                     (default is 1000)
    -u   --password_end              Number up-to which you want to check for password
                                     (default is 10000)
    -t,  --time                      time between two
                                     successive attack
                                     (default is 0.5 sec)                                 


# FAQ

Coming soon...


# COPYRIGHT

CyberoamMayhem is released under MIT license.
