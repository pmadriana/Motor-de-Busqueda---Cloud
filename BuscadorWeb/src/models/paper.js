const mongoose = require('mongoose');
const db = require('../database')
const {Schema} = mongoose;

const PaperSchema = new Schema({
    id: {type: String, required: true, unique:true},
    title: {type: String, required: true},
},
{
    collection: 'papers'
}
);

module.exports = mongoose.model('paper', PaperSchema);
