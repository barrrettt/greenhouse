#!/bin/bash
source /home/barrrettt/proyectos/barrrettt/greenhouse/venv/bin/activate
python /home/barrrettt/proyectos/barrrettt/greenhouse/main.py >> /home/barrrettt/proyectos/barrrettt/greenhouse/cron.log 2>&1
