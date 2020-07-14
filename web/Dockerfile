FROM zealsec/lamp:5

EXPOSE 80 

# Install the needed PHP libraries
# ================================
RUN apt-get update; \
    apt-get install -y wget unzip; 

COPY 74ms_5.0.1.zip /tmp
RUN unzip /tmp/74ms_5.0.1.zip -d /tmp; \
    rm -rf /var/www/html; \
    mv /tmp/74ms_5.0.1 /var/www/html/; \
    touch /var/www/html/include/config.inc.php; \
    chmod a+rw -R /var/www/html/; \
    echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php; \
    rm /tmp/74ms_5.0.1.zip

RUN chmod 777 /var/www/html/Application/Common/Conf;\
    chmod 777 /var/www/html/Application/Home/View/default/Config/config_ads.php;\
    chmod 777 /var/www/html/Application/Home/Conf/config.php;\
    chmod 777 /var/www/html/ install/
