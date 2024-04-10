import React from "react";

function Note({ note, onDelete }) {
    const formattedDate = new Date(note.created_at).toLocaleDateString("en-US")
    
    return (
        <div key={note.author} className="note-container">
            <p className="note-title">{note.title}</p>
            <p className="note-content">{note.desc}</p>
            <p className="note-date">{formattedDate}</p>
            <button className="delete-button" onClick={() => onDelete(note.author)}>
                Delete
            </button>
        </div>
    );
}

export default Note