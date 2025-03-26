document.addEventListener("DOMContentLoaded",function() {
    
    document.getElementById("taskForm").addEventListener("submit",async function (event) {
        event.preventDefault()
        
        const description = document.getElementById("description").value 
        console.log(description)
        
        const taskData = {
            description: description,
            isComplete: false
        }

        const response = await fetch("http://localhost:8000/task/",
            {
                method: "POST",
                headers: {
                    "Content-type" : "application/json",
                    "Accept": "application/json"
                },
                body : JSON.stringify(taskData)
            }
        )
        await response.json()    
        console.log(response.json)
        
    })
})