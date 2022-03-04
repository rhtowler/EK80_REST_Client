#!/bin/bash

inpath="/home/camtrawl/CamtrawlAcquisition/CamtrawlServer"
outpath="/home/camtrawl/CamtrawlAcquisition/CamtrawlServer"

/usr/local/bin/protoc -I=$inpath --python_out=$outpath $inpath/CamtrawlServer.proto
