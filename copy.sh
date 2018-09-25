mkdir -p tmp/frontend
cp -R backend tmp/backend
rm -rf tmp/backend/.idea
rm -rf tmp/backend/__pycache__
rm -rf tmp/.gitignore
find . -name ".DS_Store" -delete
rm -rf tmp/backend/app/__pycache__
cp -R frontend/dist tmp/frontend/dist
cp -R docker tmp/docker
tar -czvf app.tar.gz -C tmp .
rm -rf tmp
scp app.tar.gz root@81.4.111.160:/opt/fgtd/app.tar.gz
rm app.tar.gz