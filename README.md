echo "# hello" >> README.md

git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/nstsnlmv/hello.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/nstsnlmv/hello.git
git push -u origin master