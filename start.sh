#!/usr/bin/env bash

set -e

exitpipe=/tmp/strat.wait
rm -f $exitpipe
mkfifo $exitpipe

backend_socket=/tmp/lucas.backend.socket


(
    set +e
    ./start-scrapyd.sh
    echo 'scrapyd' >$exitpipe
) &

(
    set +e
    ./start-backend.sh "$backend_socket"
    echo 'backend' >$exitpipe
) &


sleep 5
touch /tmp/app-initialized


read exit_process <$exitpipe
echo "at=exit process=$exit_process"
