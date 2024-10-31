

<template>
  <div class="dashboard">
    <!-- Sidebar -->
    <aside class="sidebar">
      <h2>ERP Admin</h2>
      <nav>
        <ul>
          <li><router-link to="/">Dashboard</router-link></li>
          <li><router-link to="/analytics">Analytics</router-link></li>
          <li><router-link to="/reports">Reports</router-link></li>
          <li><router-link to="/users">Users</router-link></li>
          <li><router-link to="/settings">Settings</router-link></li>
          <li><router-link to="/about">About</router-link></li>
        </ul>
      </nav>
    </aside>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Header -->
      <header class="header">
        <h1>Dashboard</h1>
        <button class="logout-button" @click="logout">Logout</button>
      </header>

      <!-- Main Content Section -->
      <section class="widgets">
        <router-view />
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  methods: {
    logout() {
      // Replace this with actual logout logic
      alert("Logged out");
    }
  }
};
</script>

<style scoped>
/* Reset basic styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Main layout */
.dashboard {
  display: flex;
  min-height: 100vh;
}

/* Sidebar */
.sidebar {
  width: 250px;
  background-color: #2e3a4e;
  color: #fff;
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.sidebar h2 {
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.sidebar nav ul {
  list-style-type: none;
}

.sidebar nav ul li {
  margin-bottom: 15px;
}

.sidebar nav ul li a {
  color: #fff;
  text-decoration: none;
  font-size: 1.1rem;
}

.sidebar nav ul li a:hover {
  color: #007bff;
}

/* Main Content */
.main-content {
  flex-grow: 1;
  padding: 20px;
  background-color: #f4f6f9;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 0;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

.header h1 {
  font-size: 1.8rem;
  color: #333;
}

.logout-button {
  padding: 8px 16px;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.logout-button:hover {
  background-color: #0056b3;
}

/* Widgets */
.widgets {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}

.widget {
  width: calc(50% - 10px);
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.widget h2 {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 10px;
}

.widget p {
  font-size: 1.5rem;
  color: #007bff;
}

/* Responsive Design */
@media (min-width: 768px) {
  .widget {
    width: calc(25% - 15px);
  }
}
</style>




<!-- <script>
import axios from 'axios';

export default {
  name: 'AboutPage',
  data() {
    return {
      teamMembers: [], 
      apiError: null 
    };
  },
  created() {
    // Fetch team members data from an API endpoint
    this.fetchTeamMembers();
  },
  methods: {
    async fetchTeamMembers() {
      try {
        const response = await axios.get('https://api.example.com/team');
        this.teamMembers = response.data;
      } catch (error) {
        this.apiError = 'Failed to load team members. Please try again later.';
        console.error(error);
      }
    },
    showTeamMember(member) {
      alert(`Name: ${member.name}, Role: ${member.role}`);
    }
  }
};
</script> -->
