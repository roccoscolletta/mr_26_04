# Questo script ridà a te (utente WSL) la proprietà dei file creati da Docker (root)
sudo chown -R $USER:$USER ros_ws/
echo "Permessi ripristinati per la cartella ros_ws!"