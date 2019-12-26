import React, { Component } from 'react';
import axios from 'axios';
class AddBrand extends Component{
  constructor(props){
      super(props);
      this.state={
        text: '',
      }
      this.addItem = this.addItem.bind(this)
  }
  addItem() {
    let text = this.state.text;
    this.props.brandinfo(text);
    this.setState({
      text:''
    })
  }
  render(){
      return(
          <div className=''>
               <div className='form'>
                  <input type='text'  value={this.state.text} onChange={(event) =>
                     this.setState({text:event.target.value})} placeholder='Enter Brand Name...' />
                  <button onClick={this.addItem}>Add</button>
               </div>
          </div>
      )
  }
}
class Brand extends Component {
  constructor(props){
    super(props);
    this.state={
      text:'',
      name:[
        {
          "id": 2,
          "name": "Reebok"
      },
      {
          "id": 3,
          "name": "Apple"
      },
      {
          "id": 4,
          "name": "Amazon"
      }
      ]
    }
    this.addProduct=this.addProduct.bind(this);
    this.refreshList=this.refreshList.bind(this);
    // this.componentDidMount=this.refreshList.bind(this);
  }
  addProduct(text)
  {
    // this.setState({
    //   students: [...this.state.students,text]
    // });
    console.log(text);
    axios.post("http://127.0.0.1:8000/brands/",{name: text}).then(res => {
      this.refreshList();
    });
  }
  refreshList() {
    axios.get("http://127.0.0.1:8000/brands/")
    .then(res => {
      this.setState({ name: res.data });
    });
  }
  componentDidMount() {
    this.refreshList();
  }
  render() {
    return (
      <div className="App">
        <AddBrand brandinfo={this.addProduct}/>
        <table >
          <thead>
          <tr className="table-row">
            <th >NAME</th>
          </tr>
          </thead>
          <tbody>
            {this.state.name.map((item,index)=>(
            <tr key={index} >
                <td>{item.name}</td>
              </tr>
          ))}
       </tbody>
       </table>
      </div>
    );
  }
}
export default Brand;
