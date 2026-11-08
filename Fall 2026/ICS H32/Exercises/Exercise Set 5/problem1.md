# Problem 1

## 1. A scenario in which HTTPE would be better

HTTPE is better when proving the server's identity is either impossible or costs more than the risk it removes.

For example, a home router or Internet connected device is one such device. It serves its administrative page using only an IP address within the LAN. Thus, no certificate authority will give it a certificate, while HTTPS would just mean warning message from the browser, which users usually ignore. However, the administrative password is sent via the same wireless signal that a neighbor can also capture. HTTPE encrypts the password but ignores the identity problem, which was solved in advance by the user.

## 2. A scenario in which HTTPS would be better

HTTPS is preferable when the attacker can do more than just listening, which practically speaking means anything to do with password, money, or something you plan on executing once you have downloaded it. Since there is no authentication mechanism built into HTTPE, the man in the middle can provide his own key and decrypt/modify/encrypt the message before passing it onto the client.
