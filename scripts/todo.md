# TODO List

*   Start CUPS
*   Fix kwallet start for hyprland
    *   /etc/pam.d/sddm
    ```shell
    auth    optional     pam_kwallet5.so
    session optional     pam_kwallet5.so
    ```
    *   /etc/environment
    ```shell
    SSH_ASKPASS=/usr/bin/ksshpass
    SSH_ASKPASS_REQUIRE=prefer
    ```
    add ```exec-once = /usr/lib/pan_kwallet_init``` to Hyprland config
*   Programs to add
    *   rog
        *    power-profiles-daemon
        *    asusctl
        *    supergfxctl
        *    rog-control-center
    *   bat
    *   eza
*   enpass-bin needs systemd service configuration and start


