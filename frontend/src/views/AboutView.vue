<template>
  <div class="about">
    <header class="about-header">
      <h1>About Us</h1>
      <p>Learn more about our team and mission.</p>
    </header>

    <section class="about-content">
      <article v-for="member in teamMembers" :key="member.id" @click="showTeamMember(member)">
        <h2>{{ member.name }}</h2>
        <p>{{ member.role }}</p>
      </article>
    </section>

    <footer class="about-footer">
      <p>Contact us at <a href="mailto:info@company.com">info@company.com</a></p>
    </footer>
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
.about {
  padding: 20px;
  text-align: center;
}

.about-header h1 {
  font-size: 2.5rem;
  color: #333;
}

.about-content {
  margin: 20px 0;
}

.about-content article {
  margin-bottom: 15px;
  cursor: pointer;
  transition: transform 0.2s;
}

.about-content article:hover {
  transform: scale(1.05);
}

.about-footer {
  margin-top: 20px;
}

.about-footer a {
  color: #007bff;
  text-decoration: none;
}

/* Responsive Styles */
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .about-content {
    display: flex;
    justify-content: space-around;
  }

  .about-content article {
    width: 45%;
  }
}
</style>
