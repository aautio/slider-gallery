#!/usr/bin/env bash

set -eu

fswebcam -r 1280x720 --jpeg 85 -D 1 "static/%Y-%m-%dT%H:%M:%S %Z.jpg"