git add .
$commitMessage = Read-Host "Enter commit message"
git commit -m "$commitMessage"
git push
