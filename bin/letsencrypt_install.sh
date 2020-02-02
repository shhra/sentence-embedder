git clone https://github.com/letsencrypt/letsencrypt $HOME/letsencrypt
$HOME/letsencrypt/letsencrypt-auto certonly --standalone --email $1 --agree-tos --no-eff-email -d $2
