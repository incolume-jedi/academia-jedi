ARG OS_APP_BASE
ARG OJS_VERSION
ARG PHP_ENGINE
ARG HTTP_PROXY
ARG HTTPS_PROXY
FROM ${OS_APP_BASE:-alpine:3.11}

LABEL application="Open Journal System"
LABEL maintainer="Public Knowledge Project <marc.bria@gmail.com>"

WORKDIR /var/www/html

# When using Composer, disable the warning about running commands as root/super user
ENV COMPOSER_ALLOW_SUPERUSER=1  \
	SERVERNAME="localhost"      \
	HTTPS="on"                  \
	HTTP_PROXY=${HTTP_PROXY:-}  \
	HTTPS_PROXY=${HTTPS_PROXY:-}  \
	PHP_ENGINE=${PHP_ENGINE:-php7}     \
	OJS_VERSION=${OJS_VERSION:-3_2_1-4} \
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
	${PHP_ENGINE}			\
	${PHP_ENGINE}-apache2	\
	runit

# PHP extensions
ENV PHP_EXTENSIONS	\
    ${PHP_ENGINE}-bcmath		\
    ${PHP_ENGINE}-bz2		\
    ${PHP_ENGINE}-calendar	\
    # ${PHP_ENGINE}-Core		\
    ${PHP_ENGINE}-ctype		\
    ${PHP_ENGINE}-curl		\
    # ${PHP_ENGINE:-php7}-date		\
    ${PHP_ENGINE}-dom		\
    ${PHP_ENGINE}-exif		\
    ${PHP_ENGINE}-fileinfo	\
    # ${PHP_ENGINE}-filter		\
    ${PHP_ENGINE}-ftp		\
    ${PHP_ENGINE}-gd		    \
    ${PHP_ENGINE}-gettext	\
    # ${PHP_ENGIN}-hash		\
    ${PHP_ENGINE}-iconv		\
    ${PHP_ENGINE}-intl		\
    ${PHP_ENGINE}-json		\
    # ${PHP_ENGINE}-libxml		\
    ${PHP_ENGINE}-mbstring	\
    ${PHP_ENGINE}-mysqli		\
    ${PHP_ENGINE}-opcache	\
    ${PHP_ENGINE}-openssl	\
    ${PHP_ENGINE}-pcntl		\
    # ${PHP_ENGINE}-pcre		\
    # ${PHP_ENGINE}-PDO		\
    ${PHP_ENGINE}-pdo_mysql	\
    ${PHP_ENGINE}-pdo_pgsql	\
    ${PHP_ENGINE}-pdo_sqlite	\
    ${PHP_ENGINE}-pgsql		\
    ${PHP_ENGINE}-phar		\
    ${PHP_ENGINE}-posix		\
    # ${PHP_ENGINE}-readline	\
    # ${PHP_ENGINE}-Reflection	\
    ${PHP_ENGINE}-session	\
    ${PHP_ENGINE}-shmop		\
    ${PHP_ENGINE}-simplexml	\
    ${PHP_ENGINE}-sockets	\
    # ${PHP_ENGINE}-SPL		\
    ${PHP_ENGINEphp7}-sqlite3	\
    # ${PHP_ENGINE}-standard	\
    ${PHP_ENGINE}-sysvmsg	\
    ${PHP_ENGINE}-sysvsem	\
    ${PHP_ENGINE}-sysvshm	\
    ${PHP_ENGINE}-tokenizer	\
    ${PHP_ENGINE}-wddx		\
    ${PHP_ENGINE}-xml		\
    ${PHP_ENGINE}-xmlreader	\
    ${PHP_ENGINE}-xmlwriter	\
    ${PHP_ENGINE}-xsl		\
    ${PHP_ENGINE}-zip		\
    ${PHP_ENGINE}-zlib

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
