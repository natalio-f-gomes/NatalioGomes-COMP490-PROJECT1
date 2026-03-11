# Author: Natalio Gomes
#### Class: COMP 490
#### Section: 003


- **gui/** → Desktop GUI application for creating, reading, updating, and deleting rooms  
  → When a room is deleted, it automatically generates a report in `Report/report.csv`
- **RoomBookingServer/** → Django REST backend server (cloned from the forked repository)


## Prerequisites

- Git
- Python 3.11
- pyenv
- pip



## RoomBookingServer Setup

### 1. RoomBookingServer

```bash
# 1. Enter the server directory
cd RoomBookingServer
# 2. Create and activate virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate    # Linux/macOS
# or
# .venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt    
# 4. Apply migrations & create superuser
python manage.py migrate
python manage.py createsuperuser
# make sure to create the super user with the credentials provided by the professor

# 5. Run development server
python manage.py runserver
```

> **Note:** Follow the original repository's README inside `RoomBookingServer/` for any project-specific setup steps

### 2. GUI Application

```bash
cd gui
pip install -r requirements.txt
python3 main.py # python main.py on windows

```

When you delete a room through the GUI, a report is automatically appended to `gui/Report/report.csv`.

## How I deployed the code to digital ocean

1. Created a DigitalOcean droplet (Ubuntu)
2. Generate an SSH key locally
   ```bash
   ssh-keygen -t ed25519 -C "studentname@student.bridgew.edu"
   ```
3. Add the public key when creating the droplet or via DigitalOcean dashboard
4. SSH into the droplet
   ```bash
   ssh root@droplet-public-ipv4
   ```
5. Create a non-root user 
   ```bash
   adduser deploy
   usermod -aG sudo deploy
   ```
6. Allow the port the app will use
   ```bash
   sudo ufw allow 8000
   sudo ufw enable
   ```
7. Install Gunicorn
   ```bash
   sudo apt update
   sudo apt install python3-venv python3-pip
   ```
8. Added the droplet public IP address in the allowed hosts in the RoomBookingServer

9. Create systemd service
    ```bash
    sudo nano /etc/systemd/system/gunicorn.service
    ```

    ```ini
    [Unit]
    Description=Gunicorn instance for Room Booking Django app
    After=network.target

    [Service]
    User=deploy
    Group=www-data
    WorkingDirectory=/home/deploy/RoomBookingServer
    Environment="PATH=/home/deploy/RoomBookingServer/.venv/bin"
    ExecStart=/home/deploy/RoomBookingServer/.venv/bin/gunicorn \
              --workers 3 \
              --bind 0.0.0.0:8000 \
              meeting_room_booking.wsgi:application

    [Install]
    WantedBy=multi-user.target
    ```
   
10. Enable and start the service
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start gunicorn
    sudo systemctl enable gunicorn
    sudo systemctl status gunicorn
    ```
