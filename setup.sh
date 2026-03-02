rm -fr image.raw
CNAME=fedora-pi-builder-$RANDOM
docker rmi spin-pi-fedora-builder
docker build -t spin-pi-fedora-builder .
docker run -it --privileged=true --name $CNAME spin-pi-fedora-builder
docker cp $CNAME:/root/image.raw .
docker rm $CNAME
docker rmi spin-pi-fedora-builder