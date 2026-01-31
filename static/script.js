function toggleTheme() {
    document.body.classList.toggle("dark");
    document.body.classList.toggle("light");
}

function addTask() {
    const task = document.getElementById("task").value;
    const energy = document.getElementById("energy").value;

    fetch('/add_task', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ task, energy })
    }).then(loadTasks);
}

function loadTasks() {
    fetch('/tasks')
        .then(res => res.json())
        .then(data => {
            let html = '';
            data.forEach(t => {
                html += `
                <div class="task ${t.energy}">
                    ${t.task} | ${t.energy} | ${t.status}
                    <select onchange="updateStatus(${t.id}, this.value)">
                        <option>Pending</option>
                        <option>In Progress</option>
                        <option>Completed</option>
                    </select>
                    <button onclick="deleteTask(${t.id})">Delete</button>
                </div>`;
            });
            document.getElementById("tasks").innerHTML = html;
        });
}

function updateStatus(id, status) {
    fetch('/update_task', {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ id, status })
    }).then(loadTasks);
}

function deleteTask(id) {
    fetch(`/delete_task/${id}`, { method: 'DELETE' })
        .then(loadTasks);
}

function generatePlan() {
    fetch('/generate_plan', {
        method: 'POST'
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("score").innerText = data.score;

        let html = '';
        data.timeline.forEach(b => {
            html += `<div class="block ${b.type}">
                        ${b.task} - ${b.type} (${b.duration} min)
                     </div>`;
        });
        document.getElementById("timeline").innerHTML = html;
    });
}

loadTasks();

