#!/bin/bash
result=`lsof -i:8000|grep '\s\d+\s'`
echo $result
pid=`grep \s \d\s $result`
echo $pid
