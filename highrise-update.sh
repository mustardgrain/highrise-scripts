#!/bin/bash

if [ "$LOCAL_DEV_DIR" = "" ] ; then
  LOCAL_DEV_DIR=$HOME/dev
fi

if [ "$VIRTUALENVWRAPPER_HOOK_DIR" = "" ] ; then
  VIRTUALENVWRAPPER_HOOK_DIR=$HOME/.virtualenvs
fi

cd $LOCAL_DEV_DIR/mustardgrain/highrise-scripts
git pull

. $VIRTUALENVWRAPPER_HOOK_DIR/highrise-scripts/bin/activate

echo "Reminding..."
./highrise-remind.py
echo "Cleaning invalids..."
./highrise-clean-invalid-companies.py
