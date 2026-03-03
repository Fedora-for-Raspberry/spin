FROM --platform=linux/arm64 fedora:latest AS fedora-build
WORKDIR /root/
RUN yes | dnf install -y jq procps-ng dtc openssl gcc-aarch64-linux-gnu wget rpmdevtools rpmlint glibc-gconv-extra e2fsprogs dosfstools parted kpartx squashfs-tools ncurses-devel gnutls-devel openssl-devel-engine nano cpio rsync cmp bc bison flex openssl-devel kernel-devel gcc g++ make python3 git xz tar
COPY . .
CMD [ "/root/build" ]