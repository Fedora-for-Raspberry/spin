FROM --platform=linux/arm64 AS fedora-build
WORKDIR /root/
COPY ffr-build.tar.gz .
COPY build .
CMD ["/root/build"]