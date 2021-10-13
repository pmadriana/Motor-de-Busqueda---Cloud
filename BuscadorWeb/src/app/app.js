import React, {Component} from 'react';

class App extends Component{
    constructor(){
        super();
        this.state = {
            title: '',
            rank: '',
            tasks:[]
        };
        this.addTask=this.addTask.bind(this);
        this.handleChange=this.handleChange.bind(this);
    }
    addTask(e){
        e.preventDefault();
        fetch('/api/tasks',{
            method: 'POST',
            body: JSON.stringify(this.state),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
            .then(res=>res.json())
            .then(data =>{
                this.setState((state, props)=>{
                    return {tasks: data}
                });
                console.log(this.state.tasks);
                
            })
            .catch(err=>console.error(err));
       
    }

   
    handleChange(e){
        const {name, value} = e.target;
        this.setState({
            [name]: value
        });
    }
    render()
    {
        return(
            <div>
                
                <nav className = "light-blue darken-4">
                <div className="container">
                     <div className="nav-wrapper">
                        <a> Motor de Busqueda</a>
                    </div>
                </div>
                </nav>


                <div className="container">
                <div className="card">
                <div className="card-content">
                <form onSubmit={this.addTask} method="$POST">
                    <div className="row">
                    <div className="input-field ">
                        <input name="word" onChange={this.handleChange} type="text" placeholder="Ingresa palabra" autoFocus/>
                    </div>
                    </div>

                    <button type="submit" className="btn light-blue darken-4">
                    Buscar
                    </button>
                </form>
                </div>
                </div>
                </div>

                <div className="container" >
                    <table>
                        <thead>
                            <tr>
                                <th>Title</th>
                                <th>Rank</th>
                            </tr>
                        </thead>
                        <tbody>
                            {
                                this.state.tasks.map(task => {
                                    return (
                                        <tr>
                                            <td>{task.title}</td>
                                            <td>{task.rank}</td>
                                        </tr>
                                    )
                                })
                            }
                        </tbody>
                    </table>

                </div>

            </div>
        )
    }
}

export default App;