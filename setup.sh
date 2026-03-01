rm -fr image.raw ffr-build.tar.gz
tar czvf ffr-bulid.tar.gz ffr-build
CNAME=fedora-pi-builder-$RANDOM
docker rmi spin-pi-fedora-builder
docker build -t spin-pi-fedora-builder .
docker run -it --privileged=true --name $CNAME spin-pi-fedora-builder
docker cp $CNAME:/root/image.raw .
docker rm $CNAME
docker rmi spin-pi-fedora-builder