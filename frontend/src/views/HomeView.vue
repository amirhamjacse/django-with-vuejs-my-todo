<template>
<div class="card">
  <!-- <img :src="image" alt="Card Image" /> -->
  <div class="card-content">
    <router-link to="/tasklist">
    <h2 class="card-title">{{ title }} Task List</h2>
    <p class="card-description">{{ description }}</p>
    <a :href="link" class="card-btn">{{ buttonText }} Click Here</a>
  </router-link>
  </div>
</div>
  <div class="card">
    <!-- <img :src="image" alt="Card Image" /> -->
    <div class="card-content">
      <h2 class="card-title">{{ title }}</h2>
      <p class="card-description">{{ description }}</p>
      <a :href="link" class="card-btn">{{ buttonText }} Button</a>
    </div>
  </div>
  <div class="card">
    <!-- <img :src="image" alt="Card Image" /> -->
    <div class="card-content">
      <h2 class="card-title">{{ title }}</h2>
      <p class="card-description">{{ description }}</p>
      <a :href="link" class="card-btn">{{ buttonText }} Button</a>
    </div>
  </div>
  <div class="card">
    <!-- <img :src="image" alt="Card Image" /> -->
    <div class="card-content">
      <h2 class="card-title">{{ title }}</h2>
      <p class="card-description">{{ description }}</p>
      <a :href="link" class="card-btn">{{ buttonText }} Button</a>
    </div>
  </div>
  <div class="card">
    <!-- <img :src="image" alt="Card Image" /> -->
    <div class="card-content">
      <h2 class="card-title">{{ title }}</h2>
      <p class="card-description">{{ description }}</p>
      <a :href="link" class="card-btn">{{ buttonText }} Button</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AboutPage',
  data() {
    return {
      teamMembers: [], // Holds team data from the API
      apiError: null // Tracks any error from the API call
    };
  },
  created() {
    // Fetch team members data from an API endpoint
    this.fetchTeamMembers();
  },
  methods: {
    async fetchTeamMembers() {
      try {
        const response = await axios.get('https://api.example.com/team'); // Replace with actual API URL
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
</script>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.card {
  width: 300px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 20px;
}

.card-title {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 10px;
}

.card-description {
  font-size: 0.9em;
  color: #555;
  margin-bottom: 20px;
}

.card-btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: #fff;
  text-align: center;
  border-radius: 4px;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.card-btn:hover {
  background-color: #45a049;
}
</style>