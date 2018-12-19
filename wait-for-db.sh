#!/bin/sh

cmd="$@"

sleep 15


>&2 echo "Postgres is up - executing command"
exec $cmd

