#!/bin/sh
# stop on any error
set -e

# bridge TCP port 1337 to our Python script
exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /app/chall.py"
