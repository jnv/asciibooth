#!/bin/bash
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cmd="cd $DIR; python3 -m asciibooth"

exec mrxvt -cf "$DIR/mrxvtrc" -e /bin/sh -c "$cmd"
