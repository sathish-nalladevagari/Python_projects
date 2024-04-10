import { useEffect, useState } from "react"
import api from "../api"
import Note from "./Note"


function Home() {
  const [notes , setNotes] = useState([])
  const [title, setTitle] = useState("")
  const [desc , setDesc] = useState("")

  useEffect(()=>{
    getNotes()
  },[])

  const getNotes = () =>{
    api.get("/api/note/")
    .then((res) => res.data)
    .then((data)=> {
      setNotes(data)
      console.log(data)
    })
    .catch((err) => alert(err))
  }
  const deleteNote = (id) => {
    console.log(id)
    api.delete(`/api/note/delete/${id}/`)
        .then((res) => {
            if (res.status === 204) alert("Note deleted!");
            else alert("Failed to delete note.");
            getNotes();
        })
        .catch((error) => alert(error));
};
  const createNote = (e) =>{
      e.preventDefault();
      api.post("/api/note/", {title , desc})
      .then((res)=>{
        if (res) alert("Note created")
        
        getNotes();
      })
      .catch((err) => alert(err))
    }
  
  return (
    <div>
            <div>
                <h2>Notes</h2>
                {notes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.author} />
                ))}
            </div>
            <h2>Create a Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="content">Desc:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={desc}
                    onChange={(e) => setDesc(e.target.value)}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
  )
}

export default Home