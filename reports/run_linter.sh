#!/bin/bash
pylint ./app/**/*.py --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" --reports=n > ./reports/pylint.txt