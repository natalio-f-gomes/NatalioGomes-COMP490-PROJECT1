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

# DigitalOcean Droplet Setup & GitHub Actions Deployment Guide

This guide walks through how I set up DigitalOcean droplet, configuring a Django application with Gunicorn, and automating deployment via GitHub Actions.

---

## Step 1 — Connect to the Droplet from Your Personal Computer

### 1.1 Generate an SSH Key (if you don't have one)

Run this on your **local machine**:

```bash
ssh-keygen -t ed25519 -C "email@student.bridgew.edu"
```

This creates two files:
- `~/.ssh/id_ed25519` —  **private key** (never share this)
- `~/.ssh/id_ed25519.pub` —  **public key**

### 1.2 Copy Your Public Key to the Droplet
when creating a droplet, add this ssh key

### 1.3 Connect to the Droplet

```bash
ssh root@droplet_ip
```

---

## Step 2 — Create a Deploy User


```bash
# Create the user
adduser deploy

# Grant sudo privileges
usermod -aG sudo deploy

# Copy root's SSH keys so the new user can also connect via SSH
rsync --archive --chown=deploy:deploy ~/.ssh /home/deploy

# Set correct permissions
chmod 700 /home/deploy/.ssh
chmod 600 /home/deploy/.ssh/authorized_keys
```

### 2.1 Grant Passwordless Sudo so GithUB actions can act in your behalf


```bash
echo "deploy ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/deploy
chmod 440 /etc/sudoers.d/deploy
```

### 2.2 Connect as `deploy` user

From your **local machine**:

```bash
ssh deploy@droplet_ip
```

---

## Step 3 — System Setup & Install Dependencies


```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y \
  python3 python3-pip python3-venv git nginx
```

---

## Step 4 — Prepare the Project Directory & Virtual Environment
 
The project files are **not cloned manually**. They are pushed automatically to the droplet by GitHub Actions via `rsync` on every deployment. However, you need to do a **one-time setup** of the virtual environment on the droplet after the first deployment runs.
 
### 5.1 After the first GitHub Actions run, SSH into the droplet and run:
 
```bash
cd /home/deploy/RoomBookingServer
 
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate
 
# Install dependencies including gunicorn
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn
 
# Save gunicorn to requirements.txt so CI installs it too
pip freeze > requirements.txt
```

---
 
## Step 5 — Configure Django Settings
 
```bash
# Run database migrations
python3 manage.py migrate
 
# Collect static files
python3 manage.py collectstatic --noinput
 
# Create an admin user
python3 manage.py createsuperuser
```
 
Make sure your Django `settings.py` has the following configured:
 
```python
ALLOWED_HOSTS = ['droplet_ip']
```
 
---
 
## Step 7 — Set Up Gunicorn as a Systemd Service
 
This is a **one-time setup** done directly on the droplet. After this, GitHub Actions will manage starting/restarting it.

 
### 7.1 Create the Gunicorn Service File
 
```bash
sudo nano /etc/systemd/system/gunicorn.service
```
 
Paste the following (replace `RoomBookingServer` with your actual wsgi module name):
 
```ini
[Unit]
Description=Gunicorn daemon for Django RoomBookingServer
After=network.target
 
[Service]
User=deploy
Group=www-data
WorkingDirectory=/home/deploy/RoomBookingServer
ExecStart=/home/deploy/RoomBookingServer/.venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind 0.0.0.0:8000 \
          meeting_room_booking.wsgi:application
 
Restart=on-failure
RestartSec=5
 
[Install]
WantedBy=multi-user.target
```
 

 
## Step 8 - Connect GitHub Actions to the Droplet
### 8.1 Add GitHub Secrets
 
Go to  GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**
 
Add the following secrets:
 
| Secret Name             | Value                                      |
|-------------------------|--------------------------------------------|
| `DIGITAL_OCEAN_SSH_KEY` | Contents of `~/.ssh/id_ed25519` (private key) |
| `DROPLET_IP_ADDRESS`    | droplet's public IP address           |
| `SERVER_ADDRESS`        | Same as droplet IP (used by tests)         |
| `SERVER_PORT`           | `8000`                                     |
 
### 8.2 Copy the Private Key Correctly
 
On your **local machine**, print the private key:
 
```bash
cat ~/.ssh/id_ed25519
```
 
Copy the **entire output** including the header and footer lines:
 
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAA...
...rest of key...
-----END OPENSSH PRIVATE KEY-----
```
 
Paste this as the value for `DIGITAL_OCEAN_SSH_KEY` in GitHub Secrets.
 

---
 
## Step 11 — GitHub Actions Workflow
 
Below is the deploy job for `.github/workflows/main.yml`. 
 
```yaml
  Sprint-4-Deploy-Server:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        working-directory: sprint_4/RoomBookingServer
        run: |
          sudo apt-get update
          python --version
          echo "::group:: Install dependencies"
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          echo "::endgroup::"
          pwd

      - name: Debug env vars
        run: |
          echo "SSH KEY is set: ${{ secrets.DIGITAL_OCEAN_SSH_KEY != '' }}"
          echo "IPADDRESS: ${{ secrets.DROPLET_IP_ADDRESS != '' }}"

      - name: Setup SSH Key
        run: |
          mkdir -p ~/.ssh
          printf '%s\n' "${{ secrets.DIGITAL_OCEAN_SSH_KEY }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
          ssh-keyscan -H ${{ secrets.DROPLET_IP_ADDRESS }} >> ~/.ssh/known_hosts

      - name: Connect to Digital Ocean Droplet
        env:
            PYTHONPATH: ${{ github.workspace }}/sprint_4/RoomBookingServer
            DITIAL_OCEAN_SSH_KEY: ${{ secrets.DIGITAL_OCEAN_SSH_KEY }}
            DROPLET_IP: ${{ secrets.DROPLET_IP_ADDRESS }}
        run: |
          ssh -i ~/.ssh/id_ed25519 deploy@$DROPLET_IP << 'EOF'
          echo "Running Server: $(pwd)"
          echo "User: $(whoami)"
          echo "Server IP address: $(hostname -I)"
          EOF

      - name: Copy RoomBookingServer to Droplet
        run: |
          rsync -avz --exclude='.git' \
                     --exclude='venv' \
                     --exclude='__pycache__' \
                     --exclude='.env' \
                     -e "ssh -i ~/.ssh/id_ed25519" \
                     ${{ github.workspace }}/sprint_4/RoomBookingServer deploy@${{ secrets.DROPLET_IP_ADDRESS }}:/home/deploy/

      - name: Deploy to DIGITAL OCEAN
        run: |
          ssh -i ~/.ssh/id_ed25519 deploy@${{ secrets.DROPLET_IP_ADDRESS }} << 'EOF'
            set -e

            cd /home/deploy/RoomBookingServer

            echo "Activating virtual environment..."
            source .venv/bin/activate

            echo "Installing requirements..."
            pip install --upgrade pip
            pip install -r requirements.txt

            echo "Running migrations..."
            python3 manage.py migrate

            echo "Restarting Gunicorn..."
            sudo systemctl daemon-reload
            sudo systemctl restart gunicorn
            sudo systemctl enable gunicorn
            sudo systemctl status gunicorn --no-pager

            echo "Done!"
          EOF
```
 
> By the way `set -e` is important — it stops the script immediately if any command fails, preventing silent partial deployments.
 
---
 
## Troubleshooting

### Gunicorn Errors
 
```bash
# Check service status
sudo systemctl status gunicorn
 
# View last 50 log lines
sudo journalctl -u gunicorn -n 50
 
# Restart manually
sudo systemctl restart gunicorn
```
 
### Verify Everything Is Running
 
```bash
sudo systemctl status gunicorn      # Gunicorn process
sudo systemctl status nginx         # Nginx process
curl http://localhost:8000          # Direct Gunicorn response
curl http://your_droplet_ip         # Response through Nginx
sudo ufw status                     # Firewall rules
```
