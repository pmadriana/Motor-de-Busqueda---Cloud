const mongoose = require('mongoose');
const db = require('../database')
const {Schema} = mongoose;

const RankSchema = new Schema({
    id: {type: String, required: true, index:true},
    rank: {type: Number, required: true},
},
{
    collection: 'ranks'
}
);

module.exports = mongoose.model('rank', RankSchema);
