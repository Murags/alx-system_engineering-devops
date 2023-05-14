# Puppet to fix typo

exec { 'fixing typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
