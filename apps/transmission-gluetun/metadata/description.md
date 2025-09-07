# Transmission + Gluetun VPN

A secure torrenting solution combining Transmission BitTorrent client with Gluetun VPN client for privacy and security.

## Features

- **Transmission**: Fast, lightweight BitTorrent client with web interface
- **Gluetun VPN**: Secure VPN tunnel protecting all traffic
- **Network Security**: All Transmission traffic routed through VPN
- **Multiple VPN Providers**: Support for AirVPN, NordVPN, Surfshark, and many others
- **WireGuard & OpenVPN**: Support for both VPN protocols
- **Flood UI**: Modern web interface for Transmission

## Configuration

### VPN Setup
Configure your VPN provider settings through the form fields:
- Select your VPN service provider
- Choose protocol (WireGuard recommended)
- Enter your VPN credentials/keys
- Select server countries

### Transmission Settings
- Set username and password for web interface
- Configure timezone and user permissions
- Downloads will be stored in `/downloads` directory

## Security

This setup ensures that:
- All BitTorrent traffic is encrypted and routed through VPN
- If VPN connection drops, Transmission loses internet access (kill switch)
- Your real IP address is never exposed to torrent peers
- DNS requests are secured through VPN

## Access

The Transmission web interface will be available on port 9091 once both containers are running and VPN is connected.

**Note**: Transmission will only be accessible when the VPN connection is active and stable.