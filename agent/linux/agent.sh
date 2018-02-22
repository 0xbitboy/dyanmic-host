#!/bin/bash
# The agent of dyanmic-host
# Created by Liaojiacan on 2.13.2018.
# Copyright (c) 2018 liaojiacan. All rights reserved.

# resolve links - $0 may be a softlink
VERSION=1.0
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
NETWORK_INTERFACE=""
HOSTNAME=$(hostname)
SERVER="127.0.0.1"
SCHEME="http"
AGENT_KEY=""
while [ ".$1" != . ]
do
  case "$1" in
    --eth )
        NETWORK_INTERFACE="$2"
        shift; shift;
        continue
    ;;
    --hostname )
        HOSTNAME="$2"
        shift; shift;
        continue
    ;;
    --scheme )
        SCHEME="$2"
        shift; shift;
        continue
    ;;
    --server )
        SERVER="$2"
        shift; shift;
        continue
    ;;

    --agent-key )
        AGENT_KEY="$2"
        shift; shift;
        continue
    ;;
    * )
        break
    ;;
  esac
done

if [ -z "$AGENT_KEY" ]; then
  echo "--agent-key:can't be empty"
  exit 2
fi


getIp(){
  ip=$(ifconfig $NETWORK_INTERFACE | awk '/inet addr/{print substr($2,6)}')
  if [ -z "$ip" ] ; then
    ip=$(ifconfig $NETWORK_INTERFACE | awk '/inet /{print $2}') 
  fi
  echo $ip
  return 1
}

reporting(){
  ip=$(getIp)
  report_url="$SCHEME://$SERVER/public/v1/agents/$AGENT_KEY"
  echo "Start reporting host info to the cloud..."
  echo "Report url:$report_url"
  echo "Agent key:$AGENT_KEY"
  echo "Hostname:$HOSTNAME"
  echo "IP:$ip"
  curl -X POST -d "host_name=$HOSTNAME&ip=$ip" $report_url 
}

# ----- Execute The Requested Command -----------------------------------------
case "$1" in
    run     )
      shift
      reporting;
      exit $?
    ;;
    sync   )

      exit $?
    ;;
    version  )
      echo $VERSION
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
