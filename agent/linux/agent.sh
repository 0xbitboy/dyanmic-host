#!/bin/bash
# The agent of dyanmic-host
# Created by Liaojiacan on 2.13.2018.
# Copyright (c) 2018 liaojiacan. All rights reserved.

# resolve links - $0 may be a softlink
ARG0="$0"
while [ -h "$ARG0" ]; do
  ls=`ls -ld "$ARG0"`
  link=`expr "$ls" : '.*-> \(.*\)$'`
  if expr "$link" : '/.*' > /dev/null; then
    ARG0="$link"
  else
    ARG0="`dirname $ARG0`/$link"
  fi
done
DIRNAME="`dirname $ARG0`"
PROGRAM="`basename $ARG0`"

# ----- Execute The Requested Command -----------------------------------------
case "$1" in
    run     )
      shift

      exit $?
    ;;
    sync   )

      exit $?
    ;;
    version  )

      exit $?
    ;;
    *       )
      echo "Unknown command: \`$1\`"
      echo "Usage: $PROGRAM ( commands ... )"
      echo "commands:"
      echo "  run               Start reporting host info to the cloud"
      echo "  sync              Start sync host file from cloud"
      echo "  version           What version of this agent are you running?"
      exit 1
    ;;
esac
