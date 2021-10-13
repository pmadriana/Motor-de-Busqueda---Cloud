const express = require('express');
const router = express.Router();

const Task = require('../models/task');
const Paper = require('../models/paper');
const Rank = require('../models/rank');

var array_papers = new Array();

function GetSortOrder(prop) {    
    return function(a, b) {    
        if (a[prop] < b[prop]) {    
            return 1;    
        } else if (a[prop] > b[prop]) {    
            return -1;    
        }    
        return 0;    
    }    
}    
   

router.get('/api/tasks', async (req, res)=>{
    
});

router.post('/api/tasks', async (req, res) =>{
    array_papers = [];
    var word = req.body.word;
    console.log(word);
    //INDICES
    var tasks = await Task.find({'word':word},{"_id":0, "word":1, "papers":1});
   
    var arr_papers=tasks[0].papers; //array con los id de papers

    var page_ranks= await Rank.find({"id": arr_papers}, {"_id":0, "id":1, "rank":1}).limit(40);
    var papers_title= await Paper.find({"id": arr_papers}, {"_id":0, "id":1, "title":1}).limit(40);

    //por cada paper veo su page rank
    for(var i=0; i<page_ranks.length; i++)
    {
        var arr_json = {"title":papers_title[i].title, "rank": page_ranks[i].rank};
        array_papers.push(arr_json);
    }

    //guardando en results
   
    console.log("guardado");
    array_papers.sort(GetSortOrder("rank"));
    res.json(array_papers);

 
});

module.exports=router;