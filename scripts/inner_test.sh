#!/bin/bash
pytest tests

export DIRECTORIES="search"

yapf -d --recursive $DIRECTORIES && pylint $DIRECTORIES
