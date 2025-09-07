# Frigate NVR

An open-source Network Video Recorder (NVR) built around real-time AI object detection using OpenCV and Tensorflow for intelligent monitoring and security.

## Features

- **AI Object Detection**: Real-time detection of people, vehicles, animals, and custom objects
- **Smart Notifications**: Intelligent alerts based on detected objects and zones
- **Live View**: Real-time camera feeds with object detection overlay
- **Recording Management**: Automatic recording triggered by events or continuous
- **Hardware Acceleration**: Support for GPU, Google Coral, and other accelerators
- **Mobile Apps**: Native iOS and Android applications
- **Home Assistant Integration**: Deep integration with Home Assistant
- **MQTT Support**: Real-time event publishing via MQTT

## Hardware Requirements

### Minimum
- CPU: Modern multi-core processor
- RAM: 4GB+ (8GB+ recommended)
- Storage: Fast SSD recommended for recordings

### Recommended Accelerators
- **Google Coral TPU**: Optimal performance for object detection
- **Intel Integrated Graphics**: Hardware acceleration for video processing
- **NVIDIA GPU**: CUDA acceleration (requires additional setup)

## Setup

### Initial Configuration
1. Access web interface on port 5000
2. Upload camera configuration file
3. Configure detection zones and objects
4. Set up recording and notification preferences

### Camera Setup
- Supports RTSP, HTTP, and other IP camera protocols
- Configurable detection areas and exclusion zones
- Multiple stream support (main, sub streams)
- Motion and object-based recording triggers

### Detection Configuration
- Pre-trained models for common objects
- Custom object detection training
- Confidence thresholds and filtering
- Zone-based detection rules

## Ports

- **5000**: Web interface and API
- **8554**: RTSP stream output
- **8555**: WebRTC streams (TCP/UDP)
- **8971**: Internal communication

## Storage Considerations

Frigate can generate significant storage requirements:
- 24/7 recording: ~1-2GB per camera per day (1080p)
- Event-only recording: Much lower storage usage
- Configurable retention policies
- Automatic cleanup of old recordings

## Performance Tips

- Use hardware acceleration when available
- Configure sub-streams for detection to reduce CPU load
- Optimize detection zones to avoid unnecessary processing
- Use fast storage (SSD) for database and recent recordings

**Note**: Requires privileged mode for hardware access and USB device passthrough for accelerators like Google Coral.