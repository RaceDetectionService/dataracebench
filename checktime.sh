#!/usr/bin/env bash

TESTS=($(grep -l main micro-benchmarks/*.cpp micro-benchmarks/*.c))
OUTPUT_DIR="results"
LOG_DIR="$OUTPUT_DIR/log"
TEST_INDEX=0
if [[ -e "$LOG_DIR/Metatime.log" ]]; then rm "$LOG_DIR/Metatime.log"; fi
echo "start time is $((`date +%s`*1000+`date +%-N`/1000000))">>"$LOG_DIR/Metatime.log"
for test in "${TESTS[@]}"; do
  testname=$(basename $test)
  id=${testname#DRB}
  id=${id%%-*}
  echo "$test has $testname and ID=$id"
  python3 Metaservice.py "$LOG_DIR/$testname.archer.parser.log" "$LOG_DIR/$testname.inspector.parser.log" "$LOG_DIR/$testname.romp.parser.log" "$LOG_DIR/$testname.tsan-clang.parser.log"
done
echo "end time is $((`date +%s`*1000+`date +%-N`/1000000))">>"$LOG_DIR/Metatime.log"
