const mongoose = require('mongoose');

mongoose.connect('mongodb://kuusack.com:27017/cloud_db')
    .then(db=>console.log('DB is connected'))
    .catch(err=>console.error(err));


module.exports = mongoose;