# create databases
CREATE DATABASE IF NOT EXISTS `masterclass_ai`;
CREATE DATABASE IF NOT EXISTS `masterclass_notifications`;
CREATE DATABASE IF NOT EXISTS `masterclass_mediator`;
CREATE DATABASE IF NOT EXISTS `masterclass_products`;
CREATE DATABASE IF NOT EXISTS `masterclass_reports`;
CREATE DATABASE IF NOT EXISTS `masterclass_subscriptions`;
CREATE DATABASE IF NOT EXISTS `masterclass_tracks`;
CREATE DATABASE IF NOT EXISTS `masterclass_users`;

# so group concats don't get truncated
SET SESSION group_concat_max_len = 4294967295;

# create pomicell user and grant rights
FLUSH PRIVILEGES;
CREATE USER IF NOT EXISTS 'masterclass'@'%' IDENTIFIED BY 'masterclass';
GRANT ALL ON *.* TO 'masterclass'@'%';
