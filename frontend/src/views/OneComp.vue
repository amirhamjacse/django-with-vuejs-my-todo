<template>
    <div>
        <h1>Testing a componant for me</h1>
        <h2 class="text-primary">
            {{ messages }}
        </h2>

        <p>Result {{ newfunc() }}</p>
    </div>
</template>

<script>
export default{
    data(){
        return {
            messages: "Testing Messages"
        }
    },
    methods: {
        newfunc(){
            let first_number = 1;
            let second_number = 2;
            let sums = first_number + second_number;
            return sums;
        }
    },
}
</script>

<style scoped>
h1{
    background-color: rgb(245, 245, 50);
    color:rgb(0, 40, 76);
}
</style>