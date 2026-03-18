import { useState, useEffect } from 'react'
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

function App() {

  const [data, setData] = useState([])

  useEffect(() => {
    fetch("http://127.0.0.1:5000/tasks")
      .then(res => res.json())
      .then(data => setData(data))
  }, [])

  const handleEdit = (id)=>{
    
  }

  return (
    <>
      <nav className="navbar navbar-light bg-primary mb-5">
        <div className="container-fluid">
          <span className="navbar-brand text-light mb-0 h1">Todo App</span>
        </div>
      </nav>

      <table className="container table">
        <thead>
          <tr>
            <th>Sr.No.</th>
            <th>Title</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>
          {data.map((task) => (
            <tr key={task.id}>
              <td>{task.id}</td>
              <td>{task.title}</td>
              <td>{task.description}</td>
              <td><EditIcon style={{ cursor: "pointer" }} onClick={()=>handleEdit(task.id)} /></td>
              <td><DeleteIcon style={{ cursor: "pointer" }}/></td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  )
}

export default App
