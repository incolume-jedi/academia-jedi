FROM ${OS_APP_BASE:-apline:3.12}

LABEL application="Open Journal System"
LABEL maintainer="Public Knowledge Project <marc.bria@gmail.com>"

WORKDIR /var/www/html

# When using Composer, disable the warning about running commands as root/super user
ENV COMPOSER_ALLOW_SUPERUSER=1  \
	SERVERNAME="localhost"      \
	HTTPS="on"                  \
	OJS_VERSION=3_2_1-4 \
	OJS_CLI_INSTALL="0"         \
	OJS_DB_HOST="localhost"     \
	OJS_DB_USER="ojs"           \
	OJS_DB_PASSWORD="ojs"       \
	OJS_DB_NAME="ojs"           \
	OJS_WEB_CONF="/etc/apache2/conf.d/ojs.conf"	\
	OJS_CONF="/var/www/html/config.inc.php"


# PHP_INI_DIR to be symmetrical with official php docker image
ENV PHP_INI_DIR /etc/php/7.3

# Basic packages
ENV PACKAGES 		\
	apache2 		\
	apache2-ssl 	\
	apache2-utils 	\
	ca-certificates \
	curl 			\
	ttf-freefont	\
	dcron 			\
	patch			\
	php8			\
	php8-apache2	\
	runit

# PHP extensions
ENV PHP_EXTENSIONS	\
    php8-bcmath		\
    php8-bz2		\
    php8-calendar	\
    # php8-Core		\
    php8-ctype		\
    php8-curl		\
    # php8-date		\
    php8-dom		\
    php8-exif		\
    php8-fileinfo	\
    # php8-filter		\
    php8-ftp		\
    php8-gd		    \
    php8-gettext	\
    # php8-hash		\
    php8-iconv		\
    php8-intl		\
    php8-json		\
    # php8-libxml		\
    php8-mbstring	\
    php8-mysqli		\
    php8-opcache	\
    php8-openssl	\
    php8-pcntl		\
    # php8-pcre		\
    # php8-PDO		\
    php8-pdo_mysql	\
    php8-pdo_pgsql	\
    php8-pdo_sqlite	\
    php8-pgsql		\
    php8-phar		\
    php8-posix		\
    # php8-readline	\
    # php8-Reflection	\
    php8-session	\
    php8-shmop		\
    php8-simplexml	\
    php8-sockets	\
    # php8-SPL		\
    php8-sqlite3	\
    # php8-standard	\
    php8-sysvmsg	\
    php8-sysvsem	\
    php8-sysvshm	\
    php8-tokenizer	\
    # php8-wddx		\
    php8-xml		\
    php8-xmlreader	\
    php8-xmlwriter	\
    php8-xsl		\
    php8-zip		\
    php8-zlib

# Required to build OJS:
ENV BUILDERS 		\
	git 			\
	nodejs 			\
	npm

# To make a smaller image, we start with the copy.
# This let us joining runs in a single layer.
COPY exclude.list /tmp/exclude.list

RUN set -xe \
	&& apk add --no-cache --virtual .build-deps $BUILDERS \
	&& apk add --no-cache $PACKAGES \
	&& apk add --no-cache $PHP_EXTENSIONS \
# Building OJS:
	# Configure and download code from git
	&& git config --global url.https://.insteadOf git:// \
	&& git config --global advice.detachedHead false \
	&& git clone --depth 1 --single-branch --branch $OJS_VERSION --progress https://github.com/pkp/ojs.git . \
	&& git submodule update --init --recursive >/dev/null \
	# Composer vudu:
 	&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer.phar \
	# To avoid timeouts with gitHub we use tokens:
	# TODO: Replace personal token by an official one.
 	# && composer.phar config -g github-oauth.github.com 58778f1c172c09f3add6cb559cbadd55de967d47 \
	# Install Composer Deps:
 	&& composer.phar --working-dir=lib/pkp install --no-dev \
 	&& composer.phar --working-dir=plugins/paymethod/paypal install --no-dev \
	&& composer.phar --working-dir=plugins/generic/citationStyleLanguage install --no-dev \
	# Node joins to the party:
	&& npm install -y && npm run build \
# Create directories
 	&& mkdir -p /var/www/files /run/apache2  \
	&& cp config.TEMPLATE.inc.php config.inc.php \
	&& chown -R apache:apache /var/www/* \
# Prepare freefont for captcha
	&& ln -s /usr/share/fonts/TTF/FreeSerif.ttf /usr/share/fonts/FreeSerif.ttf \
# Prepare crontab
	&& echo "0 * * * *   ojs-run-scheduled" | crontab - \
# Prepare httpd.conf
	&& sed -i -e '\#<Directory />#,\#</Directory>#d' /etc/apache2/httpd.conf \
	&& sed -i -e "s/^ServerSignature.*/ServerSignature Off/" /etc/apache2/httpd.conf \
# Clear the image (list of files to be deleted in exclude.list).
	&& cd /var/www/html \
 	&& rm -rf $(cat /tmp/exclude.list) \
	&& apk del --no-cache .build-deps \
	&& rm -rf /tmp/* \
	&& rm -rf /root/.cache/* \
# Some folders are not required (as .git .travis.yml test .gitignore .gitmodules ...)
	&& find . -name ".git" -exec rm -Rf '{}' \; \
	&& find . -name ".travis.yml" -exec rm -Rf '{}' \; \
	&& find . -name "test" -exec rm -Rf '{}' \; \
	&& find . \( -name .gitignore -o -name .gitmodules -o -name .keepme \) -exec rm -Rf '{}' \;

COPY root/ /

EXPOSE 80
EXPOSE 443

VOLUME [ "/var/www/files", "/var/www/html/public" ]

RUN chmod +x /usr/local/bin/ojs-start
CMD ["ojs-start"]
