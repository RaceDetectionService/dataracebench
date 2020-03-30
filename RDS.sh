#!/usr/bin/env bash

TESTS=($(grep -l main micro-benchmarks/*.cpp micro-benchmarks/*.c))
for test in "${TESTS[@]}"; do
  testname=$(basename $test)
  id=${testname#DRB}
  id=${id%%-*}
  echo "$test has $testname and ID=$id"
  curl -F 'file=@$testname' cci-pivo:5010/test?type=json
done
