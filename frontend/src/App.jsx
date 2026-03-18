import { useState, useEffect } from 'react'

function App() {

  const [data, setData] = useState({})

  useEffect(() => {
    fetch("http://127.0.0.1:5000/")
      .then(res => res.json())
      .then(data => setData(data))
  }, [])

  return (
    <>
      {data.message}
    </>
  )
}

export default App
