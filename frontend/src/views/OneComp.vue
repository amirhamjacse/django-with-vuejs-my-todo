<template>
    <div>
        <h1>Testing a componant for me</h1>
        <h2 class="text-primary">
            {{ messages }}
        </h2>

        <p>Result {{ newfunc() }}</p>
        <h1 class="bg-primary text-center pb-2">Sum of two number</h1>
        <div class="form-group">
            <input class="form-control my-2" type="text" v-model="first_number">
            <input class="form-control" type="text" v-model="second_number">
        </div>
        <button class="btn btn-success my-2" @click="sumoftwoInput">Get Result</button>
        <p class="text-danger">Result: {{ result }}</p>
    </div>
</template>

<script>
export default{
    data(){
        return {
            messages: "Testing Messages",
            first_number: '',
            second_number: '',
            result: '',
        }
    },
    methods: {
        newfunc(){
            let first_number = 1;
            let second_number = 2;
            let sums = first_number + second_number;
            return sums;
        },
        sumoftwoInput(){
            this.result = parseInt(this.first_number) + parseInt(this.second_number);
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