#!/bin/bash

cmd="$@"

>&2 echo "Run celery"
celery -A aggregator.tasks worker -B -l debug

exec $cmd
