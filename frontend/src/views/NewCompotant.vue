<template>
  <div>
    <h1>{{ message }}</h1>
    <p>Count: {{ count }}</p>
    <p>Doubled Count: {{ doubledCount }}</p>
    <button @click="increment">Increment</button>
    <button @click="resetCount">Reset</button>
  </div>
</template>


<script>
export default {
  // 1. Component Name (optional but useful for debugging and reuse)
  name: 'MyComponent',

  // 2. Props: Accepts data passed from a parent component
  props: {
    initialCount: {
      type: Number,
      default: 0
    }
  },

  // 3. Data: Defines reactive data properties specific to this component
  data() {
    return {
      count: this.initialCount, // initializing with a prop value
      message: 'Hello, Vue!'
    };
  },

  // 4. Computed: Defines derived, cached properties based on reactive data
  computed: {
    doubledCount() {
      return this.count * 2;
    }
  },

  // 5. Methods: Functions to handle actions and events
  methods: {
    increment() {
      this.count += 1;
    },
    resetCount() {
      this.count = this.initialCount;
    }
  },

  // 6. Watchers: Responds to changes in specific data properties
  watch: {
    count(newValue, oldValue) {
      console.log(`Count changed from ${oldValue} to ${newValue}`);
    }
  },

  // 7. Lifecycle Hooks: Called at specific points in the component lifecycle
  mounted() {
    console.log('Component is mounted!');
    this.greet(); // Example of calling a method on mount
  },

  // 8. Additional Methods for Lifecycle or Initial Actions
  methods: {
    greet() {
      console.log(this.message);
    }
  }
};
</script>


<style scoped>
/* Scoped CSS for the component */
button {
  margin: 5px;
  padding: 8px 16px;
}
</style>
