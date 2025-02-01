FROM lscr.io/linuxserver/webtop:arch-kde AS final

RUN <<_INSTALL_PACMAN_PACKAGES
#!/bin/bash
sudo pacman -Syu --noconfirm \
    zsh zsh-autosuggestions zsh-syntax-highlighting \
    wget curl nano git \
    kmail kmail-account-wizard \
    konqueror konversation kwalletmanager \
    merkuro kommit \
    kate kdevelop kdevelop-python kdevelop-php kdevelop-pg-qt \
    distrobox
_INSTALL_PACMAN_PACKAGES

RUN <<_INSTALL_WINDSURF_DEPENDENCIES
#!/bin/bash
sudo pacman -S --noconfirm \
    alsa-lib \
    dbus \
    expat \
    gcc-libs \
    glibc \
    libdrm \
    libx11 \
    libxcomposite \
    libxdamage \
    libxext \
    libxfixes \
    libxinerama \
    libxkbcommon \
    libxrandr \
    mesa \
    nspr \
    nss \
    gtk3 \
    xdg-utils
_INSTALL_WINDSURF_DEPENDENCIES

RUN <<_SETUP_USER_ABC
#!/bin/bash
echo "Setting up user..."
sudo usermod -s /bin/zsh abc
_SETUP_USER_ABC
