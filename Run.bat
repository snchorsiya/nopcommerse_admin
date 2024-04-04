@echo off
call venv\scripts\activate
rem pytest -s -v -m "sanity" --html test_repost.html --browser chrome
pytest -s -v -m "sanity" --html firefox_repost.html --browser firefox
rem pytest -s -v -m "regression" --html test_repost.html --browser chrome
rem pytest -s -v -m "sanity and regression" --html test_repost.html --browser chrome
rem pytest -s -v -m "sanity or regression" --html test_repost.html --browser chrome
pause