rm -fr image.raw
CNAME=fedora-pi-builder-ghcr
IMAGE=ghcr.io/fedora-for-raspberry/spin
docker rmi $IMAGE
docker pull --platform linux/amd64 $IMAGE
docker run -it --privileged=true --name $CNAME $IMAGE
docker cp $CNAME:/root/image.raw .
docker rm $CNAME
docker rmi $IMAGE