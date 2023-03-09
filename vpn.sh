#!/bin/sh +x

docker run -d \
--name=sportShop_openVpn \
--cap-add=NET_ADMIN \
-p 8181:8181 \
--device=/dev/net/tun \
-v "/$(pwd)/helpers/vpn:/data/vpn" \
--restart=unless-stopped \
ghcr.io/wfg/openvpn-client
