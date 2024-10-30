<template>
    <div class="task-list-container">
      <h2 class="task-list-title">Task List</h2>
      
      <div class="task-input">
        <input 
          v-model="newTask" 
          type="text" 
          placeholder="Add a new task" 
          @keyup.enter="addTask"
        />
        <button @click="addTask">Add</button>
      </div>
      
      <ul class="task-list">
        <li 
          v-for="task in tasks" 
          :key="task.id" 
          :class="{ 'task-item': true, 'completed': task.completed }"
        >
          <input 
            type="checkbox" 
            v-model="task.completed"
            @change="updateTask(task)"
          />
          <span class="task-text">{{ task.text }}</span>
          <button class="delete-btn" @click="deleteTask(task.id)">Delete</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newTask: '',
        tasks: ['hello', 'Yes'],
        apiUrl: 'https://api.example.com/tasks',
      };
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await axios.get(this.apiUrl);
          this.tasks = response.data;
        } catch (error) {
          console.error('Error fetching tasks:', error);
        }
      },
      async addTask() {
        if (this.newTask.trim()) {
          try {
            const response = await axios.post(this.apiUrl, {
              text: this.newTask,
              completed: false,
            });
            this.tasks.push(response.data);
            this.newTask = '';
          } catch (error) {
            console.error('Error adding task:', error);
          }
        }
      },
      async updateTask(task) {
        try {
          await axios.put(`${this.apiUrl}/${task.id}`, {
            text: task.text,
            completed: task.completed,
          });
        } catch (error) {
          console.error('Error updating task:', error);
        }
      },
      async deleteTask(id) {
        try {
          await axios.delete(`${this.apiUrl}/${id}`);
          this.tasks = this.tasks.filter(task => task.id !== id);
        } catch (error) {
          console.error('Error deleting task:', error);
        }
      },
    },
    mounted() {
      this.fetchTasks();
    },
  };
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  .task-list-container {
    width: 400px;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .task-list-title {
    font-size: 1.5em;
    color: #333;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .task-input {
    display: flex;
    margin-bottom: 20px;
  }
  
  .task-input input {
    flex: 1;
    padding: 10px;
    font-size: 1em;
    border: 1px solid #ddd;
    border-radius: 4px 0 0 4px;
    outline: none;
  }
  
  .task-input button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 1em;
    border-radius: 0 4px 4px 0;
    transition: background-color 0.3s ease;
  }
  
  .task-input button:hover {
    background-color: #45a049;
  }
  
  .task-list {
    list-style: none;
  }
  
  .task-item {
    display: flex;
    align-items: center;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    transition: background-color 0.2s ease;
  }
  
  .task-item.completed {
    background-color: #e8f5e9;
    text-decoration: line-through;
    color: #888;
  }
  
  .task-text {
    flex: 1;
  }
  
  .delete-btn {
    padding: 5px 10px;
    background-color: #e53935;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
    transition: background-color 0.3s ease;
  }
  
  .delete-btn:hover {
    background-color: #d32f2f;
  }
  </style>