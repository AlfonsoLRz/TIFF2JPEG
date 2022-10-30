for /r %%a in (*) do exiftool.exe -TagsFromFile %%~nxa "-all:all>all:all" ../Test/%%~nxa
pause