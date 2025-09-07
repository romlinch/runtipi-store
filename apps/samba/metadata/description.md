# Samba File Server

Network file sharing server using the SMB/CIFS protocol, compatible with Windows, macOS, and Linux clients.

## Features

- **Cross-Platform**: Works with Windows, macOS, Linux, and mobile devices
- **Network Discovery**: Automatic discovery via Avahi/Bonjour
- **User Management**: Configurable user accounts and permissions
- **Share Configuration**: Flexible share setup with access controls
- **Time Capsule Mode**: Can emulate Apple Time Capsule functionality
- **Security**: User-based authentication and access control

## Configuration

### Basic Setup
- Configure server model and network name
- Set up user accounts with passwords
- Define shared directories and permissions

### Network Access
- Uses host networking for optimal compatibility
- Supports SMB protocol for file sharing
- Network discovery for easy client connection

### Security
- User-based authentication required
- Configurable read/write permissions per share
- No guest access by default

## Usage

1. Configure user accounts and passwords
2. Set up shared directories
3. Connect from clients using `\\server-ip` or server name
4. Use configured credentials to access shares

## Client Connection

- **Windows**: Use `\\server-name` in File Explorer
- **macOS**: Use Finder > Connect to Server > `smb://server-name`
- **Linux**: Mount using `mount -t cifs` or file managers

**Note**: Uses host network mode for maximum compatibility with SMB discovery protocols.